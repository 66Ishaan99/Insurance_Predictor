import streamlit as st
import pandas as pd
import numpy as np
import xgboost
import datetime
import pickle

st.header("Insurance Premium Predictor")
st.subheader('Data')
df = pd.read_csv('insurance.csv')
st.dataframe(df.head())

st.subheader('Enter values for following features')
col1, col2, col3 = st.columns(3)
diabetes = col1.selectbox('Diabetes', ['Yes', 'No'])
bp = col2.selectbox('BP problems', ['Yes', 'No'])
transplants = col3.selectbox('Any transplants', ['Yes', 'No'])

col4, col5, col6 = st.columns(3)
chronic = col4.selectbox('Chronic disease', ['Yes', 'No'])
allergies = col5.selectbox('Known allergies', ['Yes', 'No'])
hist_cancer = col6.selectbox('History of cancer', ['Yes', 'No'])

age = st.slider('Age', 18, 100, step=1)
height = st.slider('Height', 140, 210, step=1)
weight = st.slider('Weight', 40, 300, step=1)
surgeries = st.selectbox('Number of Surgeries', [0, 1, 2, 3])

encode_dict = {'diabetes': {'Yes': 1, 'No': 0},
               'bp': {'Yes': 1, 'No': 0},
               'transplants': {'Yes': 1, 'No': 0},
               'chronic': {'Yes': 1, 'No': 0},
               'allergies': {'Yes': 1, 'No': 0},
               'hist_cancer': {'Yes': 1, 'No': 0}}

def pred_model(diabetes, bp, transplants, chronic, allergies, hist_cancer, age, height, weight, surgeries):
    bmi = weight / (height / 100) ** 2
    # loading the standardization model and predictive model
    num_cols = []
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
        for col in [age, weight, height, bmi]:
            num_cols.append(scaler.transform([[col]]).flatten()[0])
        
        #For testing purpose
        print(num_cols)
        
    with open('predictive_model.pkl', 'rb') as file:
        model = pickle.load(file)
    # encoding categorical features
    diabetes = encode_dict['diabetes'][diabetes]
    bp = encode_dict['bp'][bp]
    transplants = encode_dict['transplants'][transplants]
    chronic = encode_dict['chronic'][chronic]
    allergies = encode_dict['allergies'][allergies]
    hist_cancer = encode_dict['hist_cancer'][hist_cancer]

    # Create the input features array
    input_features = [[num_cols[0], diabetes, bp, transplants, chronic, num_cols[2], num_cols[1], allergies, hist_cancer, surgeries, num_cols[3]]]
    return model.predict(input_features)

if st.button('Predict Premium'):
    premium = pred_model(diabetes, bp, transplants, chronic, allergies, hist_cancer, age, height, weight, surgeries)
    st.text(f'The tentative premium price is {round(float(premium[0]),2)}')


