import pickle
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from PIL import Image
#Load Pictures
positive_pic = Image.open('positive.jpg')
negative_pic = Image.open('negative.jpg')
twitter = Image.open('twitter.jfif')
#Disposition of title and twitter icon.
col1, col2 = st.beta_columns([0.25,1])
with col1:
    st.image(twitter)
with col2:
    st.title('Your own twitter sentiment analysis web app!')
sentence = st.text_input('Paste your tweet over here and I will tell you if positive or negative:')
#Load my Logistic Regression model.
Logistic = pickle.load(open('Logreg_model.sav', 'rb'))
# Execute model based on input and show output.
if sentence:
    result = Logistic.predict([sentence])
    if result == 0:
        success = st.success('Negative tweet. Go and fight!')
        st.image(negative_pic)
        
    elif result == 1:
        success = st.success('This is a Positive tweet. Positive tweet means positive vibes. Go and spread em.')
        st.image(positive_pic)

# Random comment to test github commiting
       