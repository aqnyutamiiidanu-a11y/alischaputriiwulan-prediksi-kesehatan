import streamlit as st
import joblib
import pandas as pd

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
