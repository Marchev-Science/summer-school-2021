#!/usr/bin/env python
# coding: utf-8

# # 1.0 What's Python

# Python is written in C (actually the default implementation is called CPython)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[1]:


# -< comment

print('Hello World!')


# In[2]:


'Hello World!'


# Types of Python objects:
# 
# Integers can be negative or positive numbers. Floats are real numbers (a superset of integers, including numbers with decimals)
# - Numbers: int, float
# 
# 
# - Words: string
# 
# 
# - Bool type
# 
# Check type of a variable with the type() function:

# In[3]:


# get the type
type(1.11)


# In[4]:


#convert int and string to float:
float(55)


# In[5]:


float('1.15')


# In[6]:


#convert integer or float to string:
str(33)


# In[7]:


#convert to string
str(1.85)


# In[8]:


#Convert int to bool:
bool(1)


# In[9]:


#Convert bool to float:
float(True)


# ## 1.1 Expressions are operations among compatible data types.

# In[10]:


# Sum, multiplication, division of integers
45+55+90


# In[11]:


#multiply
3*5


# In[12]:


#divide
99//11


# In[13]:


# Division of floats
99/11


# ## 1.2  Storing variables in Python is quite easy. We can also perform operation on the stored variables.

# In[14]:


# Store value into variable
x=85


# In[15]:


# Pring value of variable
x


# In[16]:


#print
print(x)


# In[17]:


# String concatenation
y = 'Michael Jordan is ' + 'the best'


# In[18]:


# String slises
y[4:7]


# In[19]:


# Get every second element in the string
y[::2]


# In[20]:


# Get every second element in range(0 to 4)
y[0:4:2]


# In[21]:


# New line escape sequence
print('Michael Jordan is \n the best')


# In[22]:


# Tab excape sequence
print('Michael Jordan is \t the best')


# In[23]:


# Backslash as string
print('Michael Jordan is \\ the best')


# In[24]:


# Replace all letters with uppercase with upper() method
y.upper()


# In[25]:


# Replace old substring with new string with replace() method
y.replace('Michael', 'Goshko')


# In[26]:


# Find substring in the string with find() method. Shows the index of the first element of the substring. Negative output if the substring is not present.
y.find('is')


# In[27]:


#find in list
y.find('bla bla')


# In[28]:


#concatenate strings
y = 'Michael Jordan is ' + 'the best'
y


# In[29]:


# python is a calculator
n = 3*7 + 2
n


# In[30]:


#f strings
f"M.Jordan's number is {n}"


# ## 1.3 Conditions and Branching

# In[31]:


# Condition Equal, Inequality, Greater, Lower than
5==6


# In[32]:


# boolean comparison
5!=6


# In[33]:


# boolean comparison
5<6


# In[34]:


# boolean comparison
5>6


# In[35]:


# Compare strings 
'ABCD' == "BDCA"


# In[36]:


# boolean comparison
'ABCD' != "BDCA"


# In[37]:


#creating a variable
age = 25


# In[38]:


# Branching in Python
if age > 18:
    print("you can enter" )
else:
    print("you can't" )


# In[39]:


# elif statement
if age > 18:
    print("you can enter" )
elif age > 21:
    print("some statement here")
else:
    print("you can't enter" )


# In[40]:


# Logical operators AND, OR, NOT
if age >18 and age<21:
    print("You can enter, but you can't drink alcohol")


# In[41]:


#simple if or
if age<20 or age>30:
    print("You are not in your 20s")
else:
    print("You are in your 20s")


# In[42]:


# if not
if not age==18:
    print('you are not 18 years old')


# ## 1.4 Loops

# In[43]:


#range and for loop
for i in range(3):
    print(i)


# In[44]:


# while loop
i=0
while(i!=5):
    print(i)
    i+=1


# In[45]:


# list comprehensions
[i for i in range(3)]


# ## 1.5 Functions

# In[46]:


#functions
def addition(a):
    b = a + 1
    print(a, "add 1 to a:", b)
    return(b)


# In[47]:


# call the function
addition(6)


# In[48]:


# Return values
def MJ():
    print('Michael Jackson')


# In[49]:


#call without argument
MJ()


# In[50]:


#again no argument
def MJ1():
    print('Michael Jackson')
    return(None)

MJ1()


# ## 1.6 Objects and classes

# In[51]:


# Create a class 
   
class Woman:

    def __init__(self, age, hair, breasts ):
        self.age = age
        self.hair = hair
        self.breasts = breasts
        


# In[52]:


#create class
Wife = Woman(43, 'dark', 'small')


# In[53]:


#create class
Lover = Woman(19, 'blond', 'big')


# In[54]:


#check classes
Wife.age > Lover.age


# In[55]:


#check classes
if Wife.breasts != 'big':
    print('She has a nice personality!')
elif Wife.breasts == 'big':
    print('Niiiiiiiiiiiiiice!')


# In[56]:


#create def for class
def breast_size(Wife):
    
    if Wife.breasts != 'big':
        print('She has a nice personality!')
    elif Wife.breasts == 'big':
        print('Niiiiiiiiiiiiiice! GJ Bro')


# In[57]:


#return an expression based on value
breast_size(Lover)


# In[58]:


# Create a class 
   
class Woman_br:
        
    def __init__(self, age, hair, breasts ):
        
        #function inside of class function
        
        def nice_or_nah(self):
            
            if self.breasts != 'big':
                
                grade = 'She has a nice personality!'

            if self.breasts == 'big':

                grade = 'Niiiiiiiiiiiiiice! GJ Bro'

            return grade
        
        
        self.age = age
        
        self.hair = hair
        
        self.breasts = breasts
        
        self.grade = nice_or_nah(self)

        


# In[59]:


W = Woman_br(23,'amber', 'small')


# In[60]:


W.grade


# # 2.0 Numpy

# Numpy solves one essential problem very fast: array processing
# 
# It is also very fast with problems that are naturally vectorized, like matrix multiplication and linear algebra routines, vectors generation and application of fixed transformation over entire array.

# ![image.png](attachment:image.png)

# In[61]:


import numpy as np


# In[62]:


x = np.random.uniform(0, 1, size=1000000)


# In[63]:


x


# In[64]:


x.mean()


# In[65]:


x


# In[66]:


a = np.zeros(3)
a


# In[67]:


type(a)


# ## 2.1 Shape and dimensions

# In[68]:


a.shape


# In[69]:


z = np.zeros(4)
z


# In[70]:


z.shape = (2, 2)
z


# ### 2.1.1 Create arrays in memory that can later be populated with data\

# In[71]:


z = np.empty(3)
z


# ### 2.1.2 Set an array of eventy spaced numbers

# In[72]:


z = np.linspace(2, 4, 5)
z


# ### 2.1.3 Create an identity matrix

# In[73]:


z = np.identity(3)
z


# ### 2.1.4 Create array from python list

# In[74]:


list = [10,20]


# In[75]:


z = np.array(list)
z


# ### 2.1.5 Array indexing 

# In[76]:


z = np.linspace(1, 2, 5)
z


# In[77]:


print(z[0])


# In[78]:


print(z[1])


# In[79]:


print(z[-1])


# ## 2.2 2D arrays operations

# In[80]:


z = np.array([[1, 2], [3, 4]])
z


# ### 2.2.1 Indexing

# In[81]:


z[0, 0]


# In[82]:


z[1, 0]


# ### 2.2.2 Extract columns and rows

# In[83]:


z[0, :]


# In[84]:


z[:, 1]


# ## 2.3 Array methods

# In[85]:


a = np.array((4, 3, 2, 1))
a


# ### 2.3.1 mean, sort, sum, etc.

# In[86]:


a.mean()


# In[87]:


a.sum() 


# In[88]:


a.sort()
a


# In[89]:


a.max()


# ### 2.3.2 Indexing

# In[90]:


# return index of max element
a.argmax() 


# In[91]:


# cumulative sum of a elements
a.cumsum()


# In[92]:


a.cumprod()


# In[93]:


a.var()


# In[94]:


a.std()


# In[95]:


a.T


# In[96]:


#use functions above from the np namespace
np.mean(a)


# ### 2.3.3 Array operations

# In[97]:


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
a + b


# In[98]:


a * b


# In[99]:


a+10


# In[100]:


a * 10


# ## 2.4 Operations on 2D array

# In[101]:


A = np.ones((2, 2))
B = np.ones((2, 2))


# In[102]:


A


# In[103]:


B


# In[104]:


A+B


# In[105]:


A + 10


# In[106]:


# Element-wise product, not matrix product
A * B


# In[107]:


# Matrix multiplication
A @ B


# ### 2.4.1 Vectorized funcitons

# In[108]:


z = np.array([1, 2, 3])
z


# In[109]:


np.sin(z)


# In[110]:


x = np.random.randn(4)
x


# In[111]:


np.where(x > 0, 1, 0)  # Insert 1 if x > 0 true, otherwise 0


# In[112]:


x


# In[113]:


# Vectorizing a user-defined function
def f2(x):
    
    if x > 0:
        
        return 1
    
    else:
        
        return 0


# In[114]:


f = np.vectorize(f2)


# In[115]:


f(x)


# ### 2.4.2 Comparisons

# In[116]:


# Comparisons are done element-wise

z = np.array([2, 3])
y = np.array([2, 3])


# In[117]:


z == y


# In[118]:


z != y


# In[119]:


z > 3


# In[120]:


b = z > 3
b


# # 3.0 Pandas

# Pandas is a module for fast and efficient data analysis tools in Python.
# 
# - Pandas Series is a single column of data.
# - Pandas DataFrame is a several columns of data.

# ![image.png](attachment:image.png)

# ## 3.1 Loading DataFrames

# In[121]:


import pandas as pd


# In[122]:


{'col1': [1, 2], 'col2': [3, 4]}


# In[123]:


pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})


# In[124]:


df = pd.read_excel('co1.xlsx')


# In[125]:


df_path = pd.read_excel(r'C:\Users\Admin\Downloads\Revenue per server data.xlsx', sheet_name = 'Raw monthly')


# ## 3.2 Using DFs

# In[126]:


import yfinance as yf 


# In[127]:


stocks = ['AMZN', 'AAPL', 'MSFT', 'GOOG','BTC-USD']


# In[128]:


data = yf.download(stocks,  
            start="2021-01-01", 
            end="2021-07-01", 
            interval ='1d').dropna()['Adj Close']


# In[129]:


data.to_excel('Financial_data.xlsx')


# In[130]:


data


# In[131]:


data.index


# In[132]:


data.columns


# In[133]:


data.head()


# In[134]:


data.tail()


# In[135]:


#select rows and columns using their integer indexes
data.iloc[:, :]


# In[136]:


data.iloc[:5, :]


# In[137]:


data.iloc[-5:, :]


# In[138]:


data.iloc[:, 3:]


# In[139]:


data.iloc[:, -1:]


# ## 3.2 DataFrame columns

# In[140]:


#select certain columns from the dataframe
data[['AAPL','AMZN']]


# In[141]:


# create new dataframe from the selected columns
df2 = data[['AAPL','AMZN']]


# In[142]:


# rename columns
df3 = df2.rename(columns={'AAPL': 'apple','AMZN': 'Jeff Bezos Shopping Centre'})


# In[143]:


df3


# In[144]:


data['AMZN_Discount'] = data['AMZN'] * 0.9 # column multiplication


# In[145]:


data


# In[146]:


data['BTC/AMZN'] = data['BTC-USD'] / data['AMZN']
data


# In[147]:


data['Index'] = range(0,len(data))


# In[148]:


data2 = data.set_index('Index')


# In[149]:


data


# In[150]:


data.set_index('Index', inplace=True)
data


# ## 3.3 DF operations

# In[151]:


data['AMZN'].mean()


# In[152]:


data['AMZN'].std()


# In[153]:


data.info()


# In[154]:


data.describe()


# In[155]:


data.corr()


# In[156]:


data.cov()


# In[157]:


data.corr() * data.cov()


# In[158]:


pd.concat([data.corr(),data.cov()], axis=0)


# In[159]:


pd.concat([data.corr(),data.cov()], axis=1)


# ## 3.3 Lazy Plots

# In[160]:


data['BTC-USD'].plot(kind='line')


# In[161]:


data['BTC_MA'] = data['BTC-USD'].rolling(10).mean()


# In[162]:


data[['BTC-USD','BTC_MA']].plot(kind='line')


# In[163]:


from sklearn.metrics import r2_score
r2_score(data['BTC-USD'].iloc[10:], data['BTC_MA'].iloc[10:])


# # 4.0 Plotly

# In[164]:


import plotly.express as px


# ## 4.1 Bars

# In[165]:


volatility = pd.DataFrame(data[stocks].std(), columns = ['Volatility'])
volatility['Stock'] = volatility.index


# In[166]:


volatility


# In[167]:


fig = px.bar(volatility, x='Stock', y='Volatility', color = 'Stock')
fig.show()


# ## 4.2 Scatters

# In[168]:


fig = px.scatter(data, x="AAPL", y="MSFT")
fig.show()


# ## 4.3 Regplots

# In[169]:


fig = px.scatter(data, x="AAPL", y="MSFT", trendline="ols")
fig.show()


# In[170]:


results = px.get_trendline_results(fig)


# In[171]:


results.px_fit_results.iloc[0].summary()


# ## 4.4 Histogram

# In[172]:


fig = px.histogram(data, x="BTC-USD")
fig.show()


# In[173]:


df = px.data.tips()
df


# In[174]:


fig = px.histogram(df, x="total_bill", color="sex")
fig.show()


# ## 4.5 3D Graphs

# In[175]:


df = px.data.iris()
df


# In[176]:


fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()


# ## 4.6 Git gud!

# ![image.png](attachment:image.png)

# In[177]:


import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.svm import SVR #(support vector machines)

mesh_size = .02
margin = 0

df = px.data.iris()

X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']

# Condition the model on sepal width and length, predict the petal width
model = SVR(C=1.)
model.fit(X, y)

# Create a mesh grid on which we will run our model
x_min, x_max = X.sepal_width.min() - margin, X.sepal_width.max() + margin
y_min, y_max = X.sepal_length.min() - margin, X.sepal_length.max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Run model
pred = model.predict(np.c_[xx.ravel(), yy.ravel()])
pred = pred.reshape(xx.shape)

# Generate the plot
fig = px.scatter_3d(df, x='sepal_width', y='sepal_length', z='petal_width', color='species')
fig.update_traces(marker=dict(size=5))
fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
fig.show()


# # 5.0 Modeling

# ## 5.1 File 1

# In[178]:


df1 = pd.read_excel('phd_count_2000-2017.xlsx')


# In[179]:


columns = [year[:4] for year in df1.iloc[1:2,1:].values[0]]


# In[180]:


df_new = df1.iloc[2:,:].dropna()
df_new.columns = ['Date']+columns


# In[181]:


df_t = df_new.T
df_t.columns = df_t.iloc[:1,:].values[0]


# In[182]:


df_final_2000_2016 = df_t.iloc[1:,:]


# In[183]:


def clean_data(df1):
    columns = [year[:4] for year in df1.iloc[1:2,1:].values[0]]
    df_new = df1.iloc[2:,:].dropna()
    df_new.columns = ['Date']+columns
    df_t = df_new.T
    df_t.columns = df_t.iloc[:1,:].values[0]
    df_final_2000_2016 = df_t.iloc[1:,:]
    return df_final_2000_2016


# ## 5.2 File 2

# In[184]:


df2 = pd.read_excel('phd_count_2017-2021.xlsx')


# In[185]:


columns = [year[:4] for year in df2.iloc[1:2,1:].values[0]]


# In[186]:


df_new = df2.iloc[2:,:].dropna()
df_new.columns = ['Date']+columns


# In[187]:


df_t = df_new.T
df_t.columns = df_t.iloc[:1,:].values[0]


# In[188]:


df_final_2017_2020 = df_t.iloc[1:,:]


# In[189]:


df_final = pd.concat([df_final_2000_2016, df_final_2017_2020], axis = 0).fillna(0)


# In[190]:


df_final.reset_index(drop=False, inplace = True)


# In[191]:


px.scatter(df_final, x=df_final.index, y="Общо", trendline = 'ols')


# In[192]:


df_final


# ## 5.3 File 3

# In[193]:


df3 = pd.read_excel('phd_finish 2000-2017.xlsx')
df3


# In[194]:


df3_clean = clean_data(df3)


# ## 5.4 File 4

# In[195]:


df4 = pd.read_excel('phd_finish 2017-2020.xlsx')
df4 


# In[196]:


df4_clean = clean_data(df4)


# In[197]:


df_final_finish = pd.concat([df3_clean, df4_clean], axis = 0).fillna(0)


# In[198]:


df_final_finish.reset_index(drop=False, inplace = True)


# ## 5.5 Final output

# In[199]:


df_final.columns = [str(column) + "_Start" for column in df_final.columns]


# In[200]:


df_final_finish.columns = [str(column) + "_End" for column in df_final_finish.columns]


# In[201]:


df_final['index_End'] = (df_final['index_Start'].astype(int) + 3).astype(str)


# In[202]:


df_merge = pd.merge(df_final,df_final_finish, on = 'index_End', how = 'left')


# In[203]:


model_data = df_merge[['index_Start', 'Общо_Start', 'Общо_End']].set_index('index_Start')

model_data


# In[204]:


model_data[:'2017'].corr()


# In[205]:


import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=model_data[:'2017'].index, y=model_data[:'2017']['Общо_Start'],
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=model_data[:'2017'].index, y=model_data[:'2017']['Общо_End'],
                    mode='lines',
                    name='lines'))


# ## 5.6 X & Y

# In[206]:


train,test = model_data[:'2017'],model_data['2018':]


# In[207]:


X_train,Y_train, X_test, Y_test = train['Общо_Start'],train['Общо_End'],test['Общо_Start'],test['Общо_End']


# ## 5.7 Regression

# In[208]:


from sklearn.linear_model import LinearRegression


# In[209]:


reg = LinearRegression().fit(X_train.values.reshape(-1, 1), Y_train.values.reshape(-1, 1))


# In[210]:


reg.score(X_train.values.reshape(-1, 1), Y_train.values.reshape(-1, 1))


# ## 5.8 Back to da drawing board

# In[211]:


y = df_merge['Общо_End']


# In[212]:


X = df_merge.filter(regex='Start').drop(columns = ['Общо_Start'])


# ## 5.9 Data cleaning

# In[213]:


X = X.replace("-",0).astype(int)


# In[214]:


y = y.replace("-",0)


# In[215]:


X_train,X_test = X[:-3],X[-3:]


# In[216]:


Y_train,Y_test = y[:-3],y[-3:]


# ## 5.10 Model 2

# In[217]:


reg = LinearRegression(normalize=True, 
                       positive = True, 
                       fit_intercept = True).fit(X_train.values, Y_train.values.reshape(-1, 1))


# In[218]:


reg.score(X_train.values, Y_train.values.reshape(-1, 1))


# In[219]:


from sklearn.metrics import mean_absolute_percentage_error
mean_absolute_percentage_error(Y_train,reg.predict(X_train.values))


# ## 5.11 Feature importance

# In[220]:


reg.coef_[0]


# In[221]:


# get importance
importance = reg.coef_[0]


# In[222]:


fig = go.Figure([go.Bar(x=X_train.columns, y=reg.coef_[0])])

fig.update_yaxes(type="log")

fig.show()


# In[223]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=X_train['index_Start'], y=Y_train,
                    mode='lines',
                    name='X_train'))

fig.add_trace(go.Scatter(x=X_train['index_Start'], y=[x[0] for x in reg.predict(X_train.values)],
                    mode='lines',
                    name='X_predicted'))


# In[224]:


reg.predict(X_test)


# In[225]:


reg.predict(X_test).sum() / model_data.iloc[-3:]['Общо_Start'].values.sum()


# ## 5.12 Does life have meaning?

# In[226]:


import statsmodels.api as sm
model = sm.OLS(Y_train, X_train)


# In[227]:


results = model.fit(normalize=True, 
                       positive = True, 
                       fit_intercept = True)


# In[228]:


results.summary()


# In[ ]:




