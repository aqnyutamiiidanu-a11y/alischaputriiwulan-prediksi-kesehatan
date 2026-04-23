import streamlit as st
import joblib
import pandas as pd
import numpy as np
import sklearn  # Sangat penting jika Anda menggunakan model Scikit-Learn

# Load model
model = joblib.load("model.pkl")

st.title("Prediksi Kesehatan")

# INPUT SESUAI DATASET
age = st.number_input("Age")
bmi = st.number_input("BMI")
children = st.number_input("Children")

if st.button("Predict"):

    input_data = pd.DataFrame({
        "age":[age],
        "bmi":[bmi],
        "children":[children]
    })

    prediction = model.predict(input_data)

    st.success(f"Hasil Prediksi: {prediction[0]}")

try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"Error memuat model: {e}")
