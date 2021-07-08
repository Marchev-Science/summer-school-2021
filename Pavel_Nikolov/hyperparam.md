# What is a hyperparameter

## Parameters vs hyperparameters

Parameters - usually parameters of the model (e.g. regression models parameters). They are being optimized during model fitting (training)

Hyperparameters - usually parameters that control the training of the model. Interatively optimized with experiments on some training/and validation/ data.

Learning_rate
" The learning rate must be set up-front before any learning can begin. So finding the right learning rate involves choosing a value, training a model, evaluating it and trying again." - source: Google blogs 
https://cloud.google.com/blog/products/ai-machine-learning/hyperparameter-tuning-cloud-machine-learning-engine-using-bayesian-optimization


## Tuning hyperparameters

There are some techniques for hyperparameter tuning ...

### Educated Guesses based on manual experiments

The researcher/scientist choose a set of parameter values, track experiments results and try to improve model performance

MANUAL ... 

### Grid Search

Step = distance between values
n = number of parameters
k = number of values for a parameter

2D grid
*---*---*---*---*  
|   |   |   |   |  
*---*---*---*---*  
|   |   |   |   |  
*---*---*---*---*  
|   |   |   |   |  
*---*---*---*---*  

param1 - k=5
param2 - k=4
total_params_to_fit_model_with = 4*5 = 20

3D grid
no time to draw it in a text editor

param1 - k=5
param2 - k=4
param3 - k=?
total_params_to_fit_model_with = 4*5*? = 20*?


nD grid
not even possible to draw it :)

TOO GREEDY

### Random Search

parameter = Random(from_distribution)

Depend on luck

### Smarter ... evolutionary Search

1. Start with a population of models (parents)

2. Measure their performance

3. Select best models based on defined metrics (accuracy, roc_auc, f1, etc.)

4. Mutate hyperparameters and crossover to get a new population (children)

5. Train the population and measure their performance

6. Repeat from step 3 till max_population reached (other stopping criteria)

