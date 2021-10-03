from typing import ValuesView
import pandas as pd
from scipy.sparse.construct import random 
a = str(input('ENTER THE PATH/DATA.CSV :    '))
df = pd.read_csv(a)
#this program is written in such assumption that your dataset consist dependent variable at[-1] or last column from left to right
x = df.ilco[:,:-1].values  #geting independent variable in x 
y = df.iloc[:,-1].values   #getting dependent variable in y



c = len(df.columns)
print(df)
#importing modules and classes for the regression model type 

from sklearn.model_selection import train_test_split            #spliting training set and test set in x and y
from sklearn.preprocessing import StandardScaler,OneHotEncoder  #Scaling the values in range(-3,3) and OneHotEncoder-- Encoding the dependent variable
from sklearn.metrics import accuracy_score,confusion_matrix     #geting the confusion matrix and accouracy score
from sklearn.ensemble import RandomForestRegressor   #RandomForesh Regression
from sklearn.linear_model import LinearRegression   #multipleLinear Regression / Linear Regression
from sklearn.tree import DecisionTreeRegressor      #DecisionTree Regression
from sklearn.compose import ColumnTransformer       #Encoding Catagorical data

#spliting the dataset into x_train,x_test,y_train,y_test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)




    




