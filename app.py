import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Production ML App", layout="centered")
st.title("ML based Wine Classifier App")

@st.cache_resource
def load_saved_model():
    with open("catboost_wine_model.pkl", "rb") as file:
        package = pickle.load(file)
    return package["model"], package["feature_names"], package["target_names"]

model, feature_names, target_names = load_saved_model()

st.sidebar.header("Input Wine Features")

user_input = {}

default_values = [14.23, 1.71, 2.43, 15.6, 127.0, 2.8, 3.066, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0]

for i, col in enumerate(feature_names):
    val = st.sidebar.slider(
        label=col,
        min_value=float(np.floor(default_values[i] * 0.5)),
        max_value=float(np.floor(default_values[i] * 1.5)),
        value=float(default_values[i])
    )
    user_input[col] = val 

input_df = pd.DataFrame([user_input])

st.subheader("Your Input Parameters:")
st.dataframe(input_df)

if st.button("Predict Wine Class", type="primary"):
    proababilities = model.predict_proba(input_df)
    predicted_class_idx = np.argmax(proababilities)
    predicted_class_name = target_names[predicted_class_idx]
    confidence = np.max(proababilities) * 100

    st.success(f"Predicted Wine Category: **{predicted_class_name}**")
    st.info(f"Model Confidence: **{confidence:.2f}%**")