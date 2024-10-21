import streamlit as st
import pandas as pd
import datetime
import pickle

st.header(" Insurance Premium Predictor ")

st.subheader('Data')

df = pd.read_csv('insurance.csv')

st.dataframe(df.head())

st.subheader(' Enter values for following features ')

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


