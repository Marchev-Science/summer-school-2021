# tune.py

import xgb
from sklearn import metrics
import pandas as pd
import numpy as np
import random
from functools import partial

class tuner:

    def __init__(self, init_params):
        """
        This is a class for xgb hyper-parameters tunning
        Това е клас за настройка на параметрите на xgb модели чрез еволюционен алгоритъм

        Args:
            init_params (dict) : A dict 
        """

        self.min_max_xbg_params = {
            'learning_rate' : (0.01, 1.0),
            'n_estimators' : (10, 1500),
            'max_depth' : (1, 8),
            'subsample' : (0.01, 1.0),
            'colsample_bytree' : (0.01, 1.0),
            'scale_pos_weight' : (1, 100)
        }

    def mutation(self, xgb_params, num_mutations=1):
        """
        Това е метод за мутиране на парамтерите на xgb модел

        """

        xgb_params_copy = xgb_params.copy()

        for _ in range(num_mutations):
            selected_param = random.choice(list(self.min_max_xgb_params.keys()))

            if selected_param == 'learning_rate':
                mutation_value = round(np.random.uniform(-0.5, 0.5), 2)
            if selected_param == 'n_estimators':
                mutation_value = np.random.randint(-200, 200, 1)[0]
            if selected_param == 'max_depth':
                mutation_value = np.random.randint(-3, 3, 1)[0]
            if selected_param == 'subsample':
                mutation_value = round(np.random.uniform(-0.25, 0.25), 2)
            if selected_param == 'subsample':
                mutation_value = round(np.random.uniform(-0.25, 0.25), 2)
            if selected_param == 'scale_pos_weight':
                mutation_value = np.random.randint(-20, 20, 1)[0]

            mutated_value = xgb_params_copy[selected_param] + mutation_value

            if mutated_value > self.min_max_xbg_params[selected_param][1]:
                mutated_value = self.min_max_xbg_params[selected_param][1]
            elif mutated_value < self.min_max_xbg_params[selected_param][0]:
                mutated_value = self.min_max_xbg_params[selected_param][0]

            xgb_params_copy[selected_param] = mutated_value

        return xgb_params_copy


    def population_grow(self, xgb_params, population_size, num_mutations=1):
        """
        Това е метод, който да порасне една популация
        """

        mutation_part = partial(self.mutation, num_mutations=num_mutations)
        population = list(map(mutation_part, [xgb_params]*population_size))

        return population

    
    def mutate_population(self, population, replication_factor, num_mutations=1):
        """
        """

        mutation_part = partial(self.mutation, num_mutations=num_mutations)
        population = list(map(mutation_part, population*replication_factor))

        return population


    def fit_one(self, xgb_params, X, y):
        """
        """

        xgb_model = xgb.XGBClassifier(**xgb_params)
        xgb_model.fit(X, y, eval_metric='auc')

        return xgb_model

    
    def fit_population(self, population, X, y):
        """
        """

        fit_one_part = partial(self.fit_one, X=X, y=y)
        fitted_population = list(map(fit_one_part, population))

        return fitted_population

    
    def fitness(self, df, fit_metric='auc'):
        """"""
        
        max_ = df[fit_metric].max()
        cutoff = df[df[fit_metric]==max_]

        return df[df['cutoff']>= cutoff]

    
    def score_one(self, model, X, y, fit_metric='auc'):
        """"""

        pred_prob = model.predict_proba(X)[:,1]

        result_list = []

        for co in np.arange(0.01, 0.99, 0.01):
            prediction = pred_prob > co

            metrics_dict {
                'auc' : metrics.roc_auc_score(y, prediction)
                'accuracy' : metrics.accuracy_score(y, prediction)
            }

            result_list.append(metrics_dict)

        metrics_df = pd.DataFrame(result_list)
        fitness_df = self.fitness(metrics_df, fit_metric='auc')

        return fitness_df

    def score_population(self, fitted_population, X, y, fit_metric='auc'):
        """
        """

        score_one_part = partial(self.score_one, X=X, y=y, fit_metric=fit_metric)
        score_population = list(map(score_one_part, fitted_population))

        return score_population


    def survive(self, score_population, fit_metric):
        """
        """

        score_population_metric = [x.iloc[0][fit_metric] for x in score_population]

        median_metric = np.median(score_population_metric)

        survived_parents = np.where(np.array(score_population_metric) >= median_metric)

        return survived_parents
    
    
    def create_child(self, parents, dominance):
        """"""

        parent1, parent2 = parents
        params = list(parent1.keys())
        num_params_p1 = int(len(params)*dominance)

        crossover_params_parent_1 = random.sample(params, num_params)
        crossover_params_parent_2 = list(set(params) - set(crossover_params_parent_1))

        child = parent1.copy()

        for param in crossover_params_parent_2:
            child.update({param:parent2[param]})

        return child


    def create_child_population(self, parents, dominance):
        """
        """

        create_child_part = partial(self.create_child, dominance=dominance)
        children_population = list(map(create_child_part, list(prodcut(parents, parents))))

        return children_population

    
    def run_evolution(self, 
        X, 
        y, 
        X_eval, 
        y_eval, 
        seed_xgb_params, 
        seed_size=10, 
        max_generations=25, 
        early_stopping_generations=3, 
        num_initial_mutations=1, 
        num_mutations=1, 
        fit_metric='auc', 
        replication_factor=2, 
        dominance=0.5
        ):      
        """
        """

        stop = False
        num_generations_without_improvement = 0
        best_score = [0]
        generation = 0
        score_population_dfs = []

        while not(stop):

            if generation == 0:
                population = self.population_grow(seed_xgb_params, seed_size, num_initial_mutations)

            else:
                children = self.create_child_population(survivors, dominance)
                population=self.mutate_population(children, replication_factor=replication_factor, num_mutations=num_mutations)

            population_fitted = self.fit_population(population, X, y)
            score_population = self.score_population(population_fitted, X_eval, y_eval)

            population_score_df = pd.concat(score_population)

            population_score_df['generation'] = generation

            population_score_df['xgb_params'] = population

            score_population_dfs.append(population_score_df)

            survivors_ids = self.survive(score_population, fit_metric)
            survivors = [population[x] for x in survivors_ids]

            generation += 1

            best_score.append(population_score_df.sort_values(fit_metric, ascending=False).iloc[0].T[fit_metric].values[0])

            if best_score[-2] > best_score[-1]:
                num_generations_without_improvement += 1

            if num_generations_without_improvement >= early_stopping_generations:
                stop = True
            elif generation >= max_generations:
                stop = True

        return score_population_dfs



