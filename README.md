# DiamondPricePredictionProject

## Preview

![caption](app_preview1.gif)
In this project we will be predicting the bid price for the diamonds from a dataset that was part of the Udacity Bertelsmann Data Track Final Project.

## How to learn from this repository?

I have created files with numbers from 1 to 4 and you can follow along with me easily.

## Why do you need to build a frontend webiste for your Data Driven Projects?

Let's take a use case. We have built a machine learning model that predicts whether a person has lung cancer or not. We have programmed this in an IPython notebook or as an Alteryx Workflow with some training data and tested the model on some other images.

But the real question is, can we make an application that can be used by anyone in the world? No, its not possible without building a friendly interface. We cannot tell the doctor to change the code in the ipython notebook to check if the image shows that the person has cancer.

Instead what we can do to create an application where the doctor can actually upload an image, the model processes the image and tells him/her if a patient has cancer. This actually makes our application useful to the world!

In today's sesssion I will not be telling you how to make an application to detect cancer, but we will be deploying the **Diamond Price Applciation that we worked on in the Foundation Course**!

So let's get started!!

## What Package will we be using?

For this sesison we will be using the **streamlit** python package that is used to build data driven web apps using very less lines of code compared to **Flask** and **Django**. We can also display _videos_, _calendars_ and _dropdowns_ with single line of code that I will be demonstrating later.

## Step-1: Building a simple webpage

File : `1.simple_webpage.py` <br>
In this python script, we have to first download `streamlit`, `pandas`, `seaborn` and `matplotlib`.

- Streamlit : `pip install streamlit`<br>
- Pandas : `pip install pandas`<br>
- Matplotlib : `pip install matplotlib`<br>
- Seaborn : `pip install seaborn`

Then we are going to import those packages in the python script. Since we need only **Streamlit** we are going to import `streamlit as st`.

In **streamlit** the different sections of our page is defined using `beta_container`.

In our project we have four containers or sections: `siteHeader`,`dataExploration`, `videoexplanation`,`modelTraining` and `linreg`.

the `with` keyword specifies or tells `streamlit` about the container that we want to put our content in.

`st.title` is used to give a title to the section of the page and <br>
`st.write` is used to display somethin to our page that is not the title. Somewhat like a body of the container.

### How to run the file on local system?

`streamlit run 1.simple_structure.py`

The app should run on `localhost:8501`

## Step-2: Data sources and Exploratory Data Analysis

We would need `matplotlib` and `Seaborn` to plot our data and `scipy.stats` to calculate the co relation that is going to be used to plot the data.

- `pd.read_csv` as the function explains is used to import the data to our script.

- `DataFrame.shape` returns the no of rows and columns in the dataset.

- `DataFrame.head` allows us to see the first five rows of the dataset

- `DataFrame.describe` gives the values of some common statistical measures.

- `scipy.stats.pearsonr(diamonds_data['carat'],diamonds_data['price']))`
  is used to calculate the pearson correlation and the p value of carat v/s price. We can see that the co relation is high and p value is 0 because the model is actually overfitted. Which means the model is too closely fit to given set of data points.

- `plt.figure()` creates an empty area with no data being plotted.

- `sns.scatterplot(x = diamonds_data['carat'],y = diamonds_data['price'])` actually plots the data but does not display it.

- `st.pyplot(fig1)` acually displays it to the user.

- `sns.heatmap(diamonds_data.corr())` returns a heatmap of the correlation of each input feature with the oher features.

You dont need to remember all this. A simple google search will get you the answer!!

We can see that the carat v/s price has a linear relation from the scatter plot and it also has a high correlation and a ridiculously low p-value! that makes it a good fit for the model.

Next we are going to use the Random Forest Model and the Linear Regression Model to predict the price given the carat value for the new_diamonds dataset.

## Step-3: Building our Random Forest Model

You can find explanations of the Decision tree and Random Forest Models here:

<a href = "https://towardsdatascience.com/machine-learning-basics-decision-tree-regression-1d73ea003fda">Decision Trees</a>,
<a href = "https://towardsdatascience.com/machine-learning-basics-random-forest-regression-be3e1e3bb91a ">Random Forest</a>
You can find an example of the decision tree model for carat v/s price in `decisiontree.png` in above file structure.

The line

```py
from sklearn.ensemble import RandomForestRegressor
```

basically says that we are importing the RandomForestRegressor model from sklearn a python package that helps us use models with less lines of code.

In this line of code, we are converting the categorical values to numerical values of 0s and 1s so that the model can read it. This is similar to the select tool in Alteryx.

```py
new_diamonds_data = pd.get_dummies(new_diamonds_data, columns=['cut', 'color', 'clarity'])
```

We can create new columns using `beta_columns`.

Then we are going to list the features that the user can choose to inpput to the model. In this application we will stick to only one features.

In the below line we are creating a text box where the user can enter the feature. in this case carat is the default value. This is being stored in input_feature variable that is used later.

```py
input_feature = selection_col.text_input('Which feature would you like to input to the model?', 'carat')
```

This line of code allows the user to select the max depth of the model.

```py
max_depth = st.slider("What should be the max_depth of the model?",min_value=10, max_value=100, value=20, step=10)
```

This code allows the user to select either 100,200 or 300 treed for the model with the default being 100.

```py
number_of_trees = st.selectbox('How many trees should there be?', options=[100, 200, 300],index=0)
```

Now let's create the create the RandomForestRegressor class using sklearn.

```py
model = RandomForestRegressor(max_depth=max_depth,n_estimators=number_of_trees)
```

We are taking the input feature to be he one user has chosen and the target as the price.

`model.fit` is used to train our model. <br>
Basically instruct the model about what are the price values for the carat calues.

```py
model.fit(X, y)
```

Finally we are using the trained model to predict the price values for the `new_diamonds` dataset!

```py
prediction = model.predict(
  new_diamonds_data[[input_feature]])
```

## To deploy the app do the following steps

Go to <a href = "https://share.streamlit.io">Streamlit Login Page</a> and create an account threre through your github login. Then you will have to request for an invite that will allow you to share your applications using Streamlit Share. You will get a confirmation mail with the invite in 48 hours.

<br>

Now you have to create a `requirements.txt` file that will let **Streamlit** know which packages you are using for your application. To do this:

1. Install pipreqs using `pip install pipreqs`.
2. Then you have to run `pipreqs <location of your project folder>`. If you have installed pipreqs in your project folder itself run `pipreqs ./`. Now wait for a minute and check whether you have a requirements.txt file in your folder. If yes, then you are good to deploy the app, else you can search for the problem solution on Google or reach out to me on <a href = "https://www.linkedin.com/in/vedanthbaliga">LinkedIn</a>

3. Now go back to the <a href="https://streamlit.io/">Streamlit</a> webiste and click **New App**
4. Choose your project repository from the dropdown menu, select either main or master and select the file that you want to deploy. In this case `app.py`.
5. Now Click deploy and wait till the processing of the app is finished.
6. Once you can see the contents of your app, you can use the URL and share it with your friends 😊

If you liked this repo and the Study Jam Webinar, considering giving the repo a **star**!
