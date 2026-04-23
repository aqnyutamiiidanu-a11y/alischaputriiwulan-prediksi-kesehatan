import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Prediksi Kesehatan")

age = st.number_input("Umur")
bmi = st.number_input("BMI")
children = st.number_input("Jumlah Anak")

if st.button("Predict"):
    data = np.array([[age, bmi, children]])
    prediction = model.predict(data)

    st.success(f"Hasil Prediksi: {prediction[0]}")
