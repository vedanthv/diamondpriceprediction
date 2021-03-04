# Importing streamlit and a few other libraries
import scipy.stats
import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
import matplotlib.pyplot as plt

siteHeader = st.beta_container()
videoExplanation = st.beta_container()
dataSource = st.beta_container()
dataExploration = st.beta_container()
modelTraining = st.beta_container() # using Random Forest Model
linreg = st.beta_container() # Using linear regression model

# Site header
with siteHeader:
    st.title("Diamond Price Prediction ML Project")
    st.write("In this project we are going to predict the diamond prices using Random Forest and Linear regression models.")

# Video Explanation
with videoExplanation:
    st.title("Video Explanation of the Project")
    st.write("Here is an overview of my project in my own words")
    st.video("https://www.youtube.com/watch?v=CmSKVW1v0xM")

# Data Source 
with dataSource:
    st.title("Data Sources")
    st.write("In this project we are going to use two data sources. These are going to be diamonds.csv and new_diamonds.csv from the Udacity Challenge Course")

    st.write("Let's read the data and take a sneak peek at it")

    diamonds_data = pd.read_csv('diamonds.csv')

    st.write("The shape of the dataset is",diamonds_data.shape)

    st.write('The first five rows of the dataset are')
    st.write(diamonds_data.head(5))
    st.write("The description of  the dataset")
    st.write(diamonds_data.describe())
# Data Exploration
#Data Exploration
with dataExploration:
    st.title("Let's Explore Our Data!")
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
    

    st.title("Conclusion!")
    st.write('carat has a linear relation with price so it can be a good input for our linear regression model, has a low p value and a high corelation and can be used as input feature for our model')
# Model Building
with modelTraining:
    st.header("Model Training")

    st.write("In this part we are going to take the input parameters fromt the user for out model, train the model and test it!")

    diamonds_data = pd.read_csv("diamonds.csv")

    new_diamonds_data = pd.read_csv("new_diamonds.csv")

    new_diamonds_data = pd.get_dummies(new_diamonds_data, columns=['cut', 'color','clarity'])

    # Make Two Columns
    selection_col, display_col = st.beta_columns(2)

    # Let's List the features that the user can input to the model
    selection_col.text('Here is a list of features: ')

    selection_col.write(diamonds_data.columns)

    input_feature = selection_col.text_input('Which feature would you like to input to the model?', 'carat')  

    # Let user input max depth of the model
    max_depth = st.slider("What should be the max_depth of the model?", 
    min_value=10, max_value=100, value=20, step=10)

    # Let the user select the no of treees in the model
    number_of_trees = st.selectbox('How many trees should there be?', 
    options=[100,200,300], 
    index=0)

    # Training our Random Forest Model

    model = RandomForestRegressor(max_depth=max_depth, 
    n_estimators=number_of_trees)    

     
    X = diamonds_data[[input_feature]] # Predictor Variables    
    y = diamonds_data[['price']] # Target Vraiable
     
    model.fit(X, y) # Training the model
    prediction = model.predict(new_diamonds_data[[input_feature]]) # Prediction

    new_diamonds_data['price'] = prediction
    
    st.write(new_diamonds_data[['carat','price']].head(5))



# Replicating the Alteryx Workflow in our application

# Predicting Prices for our new_diamonds.csv
with linreg:
    st.title("Let's Follow the approach from the Udacity course")

    st.write("Let's follow the approach from the Udacity Course and use a linear regressor model")

#Importing our data
new_diamonds = pd.read_csv("new_diamonds.csv")

diamonds = pd.read_csv("diamonds.csv")

#Converting to Dummy Variables
diamonds = pd.get_dummies(diamonds, columns=['cut', 'color','clarity'])

new_diamonds = pd.get_dummies(new_diamonds, columns=['cut', 'color','clarity'])

# Use a linear Regressor Model
clf = linear_model.LinearRegression()


Y = diamonds.price #Target

X = diamonds.drop("price", axis=1) #Predictor

clf.fit(X,Y) #Training

Y_pred = clf.predict(new_diamonds) #Predict

bid = 0.7 * sum(Y_pred) #Calculating bid price

st.write("Our bid Price for 3000 diamonds is ",'%.2f' % bid)

st.header("View my Code on Github!")
link = '[GitHub](http://github.com/vedanthv)'
st.markdown(link, unsafe_allow_html=True)


