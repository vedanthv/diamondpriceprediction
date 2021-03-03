# Replicating the Alteryx Workflow in our application

import streamlit as st
import pandas as pd
from sklearn import linear_model

# Predicting Prices for our new_diamonds.csv

st.header("Let's Follow the approach from the Udacity course")

st.write("Let's follow the approach from the Udacity Course and use a linear regressor model")

#Importing our data
new_diamonds = pd.read_csv("new_diamonds.csv")

diamonds = pd.read_csv("diamonds.csv")

#Converting to Dummy Variables
diamonds = pd.get_dummies(diamonds, columns=['cut', 'color','clarity']) #Just like the select tool in Alteryx

new_diamonds = pd.get_dummies(new_diamonds, columns=['cut', 'color','clarity'])

# Use a linear Regressor Model
clf = linear_model.LinearRegression()


Y = diamonds[['price']] #Target

X = diamonds.drop("price", axis=1) #Predictor

clf.fit(X,Y) #Training

Y_pred = clf.predict(new_diamonds) #Predict

new_diamonds['price'] = Y_pred

bid = 0.7 * sum(Y_pred) #Calculating bid price

st.write("Our bid Price for 3000 diamonds is ",'%.2f' % bid)