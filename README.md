# DiamondPricePredictionProject

# Preview


![caption](app_preview1.gif)



In this project we will be predicting the bid price for the diamonds from a dataset that was part of the Udacity Bertelsmann Data Track Final Project.

# How to learn from this repository?

I have created files with numbers from 1 to 4 and you can follow along with me easily.

# Why Do you need to deploy your Data Driven Projects?

Let's take a use case. We have built a machine learning model that predicts whether a person has lung cancer or not. We have programmed this in an IPython notebook or as an Alteryx Workflow with some training data and tested the model on some other images.

But the real question is, can we make an application that can be used by anyone in the world? No, its not possible without building a friendly interface. We cannot tell he doctor to change the code in the ipython notebook to check if the image shows that the person has cancer. 

Instead what we can do is create an application where the doctor can actually upload an image, the model processes the image and tells him/her if a patient has cancer. This actually makes our application useful to the world!

# To deploy the app do the following steps...

Go to <a href = "https://share.streamlit.io">Streamlit Login Page</a> and create an account threre through your github login. Then you will have to request for an invite that will allow you to share your applications using Streamlit Share. You will get a confirmation mail with the invite in 48 hours.

<br>

Now you have to create a requirements.txt file that will let Streamlit know which packages you are using for your application. To do this:

1. Install pipreqs using `pip install pipreqs`.
2. Then you have to run `pipreqs <location of your project folder>`. If you have installed pipreqs in your project folder itself run `pipreqs ./`. Now wait for a miinute and check whether you have a requirements.txt file in your folder. If yes, then you are good to deploy the app, else you can search for the problem solution on Google or reach out to me on <a href = "https://www.linkedin.com/in/vedanthbaliga">LinkedIn</a>

3. Now go back to the Streamlit webiste and click 'New App'
4. Choose your project repository from the dropdown menu, select either main or master and select the file that you want to deploy. In this case `app.py`.
5. Now Click deploy and wait till the processing of the app is finished. 
6. Once you can see the contents of your app, you can use the URL and share it with your friends :)

If you liked this repo and the Study Jam Webinar, considering giving the repo a star!

