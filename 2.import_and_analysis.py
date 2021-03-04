# In this section we are going to import the data diamoonds.csv and perform simple data analysis.

# Import libraries..
import streamlit as st
import seaborn as sns
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
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
    
  
#Data Exploration
with dataExploration:
    st.header("Let's Explore Our Data!")
    st.write("In this section let us explore our data!")
    diamonds_data = pd.read_csv('diamonds.csv')

    # Gives 2 values co relation co-efficient and p-value
    
    st.write("Co relation co efficient and p value of carat v/s price",scipy.stats.pearsonr(diamonds_data['carat'],diamonds_data['price']))

    diamonds = pd.read_csv('diamonds.csv')

    diamonds = pd.get_dummies(diamonds, columns=['cut', 'color','clarity']) #Just like the select tool in Alteryx

    st.title('Scatterplot between carat and price')
    fig1 = plt.figure()
    sns.scatterplot(x = diamonds_data['carat'],y = diamonds_data['price'])
    st.pyplot(fig1)

    st.title('Correlation between features')
    fig = plt.figure()
    ax = sns.heatmap(diamonds_data.corr())
    st.pyplot(fig)
    

    st.subheader("Conclusion!")
    st.write('carat has a linear relation with price so it can be a good input for our linear regression model, has a low p value and a high corelation and can be used as input feature for our model')