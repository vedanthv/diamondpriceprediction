# In this section we are going to import the data diamoonds.csv and perform simple data analysis.

# Import libraries..
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataSource = st.beta_container()
dataExploration = st.beta_container()

# Data Source 
with dataSource:
    st.header("Data Sources")
    st.write("In this project we are going to use two data sources. These are going to be diamonds.csv and new_diamonds.csv from the Udacity Challenge Course")
    st.write("Let's read the data and take a sneak peek at it")
    diamonds_data = pd.read_csv('diamonds.csv')
    st.write(diamonds_data.head(5))
# Data Exploration
with dataExploration:
    st.header("Let's Explore Our Data!")
    st.write("In this section let us explore our data!")
    diamonds_data = diamonds_data[:1000] #Taking a subset of our data
    fig = sns.pairplot(diamonds_data)
    st.pyplot(fig)  