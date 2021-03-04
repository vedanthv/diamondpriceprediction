# Let's import libraries

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Importing data
diamonds_data = pd.read_csv("diamonds.csv")
new_diamonds_data = pd.read_csv("new_diamonds.csv")


new_diamonds_data = pd.get_dummies(new_diamonds_data, columns=[
                                   'cut', 'color', 'clarity'])

# Model Training
modelTraining = st.beta_container()

with modelTraining:
    st.header("Model Training")
    st.write("In this part we are going to take the input parameters fromt the user for out model, train the model and test it!")

   # Make Two Columns
    selection_col, display_col = st.beta_columns(2)

   # Let's List the features that the user can input to the model
    selection_col.text('Here is a list of features: ')

    selection_col.write(diamonds_data.columns)

    input_feature = selection_col.text_input(
        'Which feature would you like to input to the model?', 'carat')  # carat is the default value

   # Let user input max depth of the model
    max_depth = st.slider("What should be the max_depth of the model?",
                          min_value=10, max_value=100, value=20, step=10)

   # Let the user select the no of treees in the model
    number_of_trees = st.selectbox('How many trees should there be?',
                                   options=[100, 200, 300],
                                   index=0)

   # Training our Random Forest Model

    model = RandomForestRegressor(max_depth=max_depth,
                                  n_estimators=number_of_trees)

    X = diamonds_data[[input_feature]]  # Predictor Variables
    y = diamonds_data[['price']]  # Target Vraiable

    model.fit(X, y)  # Training the model
    prediction = model.predict(
        new_diamonds_data[[input_feature]])  # Prediction

    new_diamonds_data['price'] = prediction

    st.write(new_diamonds_data[['carat', 'price']].head(5))
