# -*- coding: utf-8 -*-
"""Multipledis_pred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1euqTArWmRN5yBguWCo3NE_BpXiZ5QFir
"""

import pickle
#!pip install -q streamlit
import streamlit as st
#!pip install -q streamlit-option-menu
import streamlit_option_menu
from streamlit_option_menu import option_menu

#Loading the saved models


with open('/content/diabetes_model.sav','rb') as f:
  diabetes_model = pickle.load(f)

with open('/content/heart_disease_model.sav','rb') as f:
  heart_disease_model = pickle.load(f)

# Creating a Streamlit app
with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
    icons = ['activity','heart','person'],
    default_index = 0)

#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):

    #Page title
    st.title('Diabetes Prediction using ML')

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

#Code for prediction
diab_diagnosis = ''

#Creating a button for prediction

if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'

        else:
            diab_diagnosis = 'The person is Not Diabetic'


st.success(diab_diagnosis)

#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):

    #Page title
    st.title('Heart Disease Prediction using ML')

    age = st.number_input('Age of the Person')
    sex = st.number_input('Sex of the Person')
    cp = st.number_input('Chest pain types')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Serum Cholestoral in mg/dl')
    fbs = st.number_input('Fasting blood sugar > 120 mg/dl')
    restecg = st.number_input('Resting Electrocardiographic results')
    thalach = st.number_input('Maximum Heart Rate achieved')
    exang = st.number_input('Exercise Induced Angina')
    oldpeak = st.number_input('ST depression induced by exercise')
    slope = st.number_input('Slope of the peak exercise ST segment')
    ca = st.number_input('Mjor vessels colored by flourosopy')
    thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

#Code for prediction
    heart_diagnosis = ''
    #Creating a button for prediction

    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person is suffering from Heart disease'

        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'


    st.success(heart_diagnosis)
