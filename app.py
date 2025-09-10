import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("crop_yield_model.pkl")

# Streamlit UI
st.set_page_config(page_title="Crop Yield Prediction", page_icon="🌾", layout="centered")

st.title("🌾 Crop Yield Prediction App")
st.write("Enter soil and weather parameters to predict crop yield (tons/hectare).")

# Input fields
N = st.number_input("Nitrogen (N)", 0, 150, 50)
P = st.number_input("Phosphorus (P)", 0, 150, 40)
K = st.number_input("Potassium (K)", 0, 150, 40)
temp = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
fertilizer = st.number_input("Fertilizer (kg/ha)", 0, 500, 100)

if st.button("Predict Yield"):
    features = np.array([[N, P, K, temp, fertilizer]])
    prediction = model.predict(features)
    st.success(f"✅ Predicted Yield: {prediction[0]:.2f} tons/ha")
