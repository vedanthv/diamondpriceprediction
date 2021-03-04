# In this part we will be 
# 1. Installing streamlit
# 2. Importing streamlit and other python packages
# 3. Building a really simple Frontend skeleton and running it locally!

# Installing streamlit
# in the terminal type pip install streamlit

# installing pandas - pip install pandas
# installing seaborn - pip install seaborn

# Importing streamlit
import streamlit as st

# Building our frontend interface

# Creating Containers  - containers are basically rows or sections on our page

siteHeader = st.beta_container()
dataSource = st.beta_container()
dataExploration = st.beta_container()
modelTraining = st.beta_container() # using Random Forest Model
linreg = st.beta_container() # Using linear regression model

# Site header
with siteHeader:
    st.title("Diamond Price Prediction ML Project")
    st.write("In this project we are going to predict the diamond prices using Random Forest and Linear regression models.")
# To run the file go to terminal and type streamlit run name_of_file.py!

# Data Source 
with dataSource:
    st.header("Data Sources")
    st.write("In this project we are going to use two data sources. These are going to be diamonds.csv and new_diamonds.csv from the Udacity Challenge Course")
# Data Exploration
with dataExploration:
    st.header("Let's Explore Our Data!")
    st.write("In this section let us explore our data!")

# Model Building
with modelTraining:
    st.header("Model Training")
    st.write("In this part we are going to take the input parameters fromt the user for out model, train the model and test it!")

#Linear Regression Method
with linreg:
    st.header("Linear Regression Model")
    st.write("Now let's use the Linear Regression model and compare the results with the result we got in the challenge course")



