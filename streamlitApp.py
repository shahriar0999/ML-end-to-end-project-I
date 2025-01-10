import streamlit as st
import requests
import os
from src import aws_s3

# Define the API endpoint
API_URL = "http://127.0.0.1:8502/"
headers = {
  'Content-Type': 'application/json'
}

st.title("ML Model Serving Over Fast Api")

model = st.selectbox("Select Model",
                     ["Sentiment Classifier", "Disaster Classifier"])


if model == 'Sentiment Classifier':
    text = st.text_area("Enter your product review (Note: If providing multiple sentiments, separate them with a comma (,))")
    text = text.split(',')
    user_id = st.text_input("Enter your user id")
    data = {
        "text": text,
        "user_id": user_id
    }
    model_api = "sentiment_analysis"

elif model == 'Disaster Classifier':
    text = st.text_area("Enter your product review (Note: If providing multiple sentiments, separate them with a comma (,))")
    text = text.split(',')
    user_id = st.text_input("Enter your user id")
    data = {
        "text": text,
        "user_id": user_id
    }
    model_api = "disaster_classifier"

# elif model=="Pose Classifier":

#     url = st.text_input("Enter Your Image Url")


#     user_id = st.text_input("Enter user id")

#     data = {"url": [url], "user_id": user_id}
#     model_api = "pose_classifier"

if st.button("Predict"):
    with st.spinner("Predicting.... Please Wait!!!!!!!!!"):
        response = requests.post(API_URL+model_api, json=data, headers=headers)

        output = response.json()

    st.write(output)