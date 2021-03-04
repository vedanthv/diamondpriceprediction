# In this section we are going to import the data diamoonds.csv and perform simple data analysis.

# Import libraries..
import streamlit as st
import seaborn as sns
import pandas as pd

dataSource = st.beta_container()
dataExploration = st.beta_container()

# Data Source 
with dataSource:
    st.header("Data Sources")
    st.write("In this project we are going to use two data sources. These are going to be diamonds.csv and new_diamonds.csv from the Udacity Challenge Course")

    st.write("Let's read the data and take a sneak peek at it")

    diamonds_data = pd.read_csv('diamonds.csv')

    st.write("The shape of the dataset is",diamonds_data.shape)

    st.write('The first five rows of the dataset are')
    st.write(diamonds_data.head(5))
    
    st.write("The description of  the dataset")
    st.write(diamonds_data.describe())

    st.write("In this section let us explore our data!")
    
  

# PLOTS IN SEABORN WORKS IN VERSIONS STREAMLIT 0.77 AND BELOW. SINCE MINE IS 0.77 VERSION I CAN'T SHOW THE PLOT RIGHT NOW :(

#Data Exploration
with dataExploration:
    st.header("Let's Explore Our Data!")
    st.write("In this section let us explore our data!")
    diamonds_data = pd.read_csv('diamonds.csv')

    fig = sns.pairplot(diamonds_data)
    st.pyplot(fig)

    st.subheader("Conclusion!")
    st.write('carat has a linear relation with price so it can be a good input for our linear regression model')