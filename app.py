# rebuild trigger
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import sklearn

# 1. Pastikan model dimuat dengan benar di luar try-except atau tangani dengan baik
# Load model
try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"Error detail: {e}")
    st.stop()  # WAJIB pakai tanda kurung () agar aplikasi benar-benar berhenti di sini
    st.stop() # Menghentikan aplikasi agar tidak lanjut ke baris prediksi yang error

# 2. Bagian input data (pastikan variabel input_data sudah didefinisikan sebelumnya)
# ... kode input Anda di sini ...

# 3. Baris prediksi
if st.button("Prediksi Sekarang"):
    prediction = model.predict(input_data)
    st.write(f"Hasil Prediksi: {prediction}")
    st.success(f"Hasil Prediksi: {prediction[0]}")
