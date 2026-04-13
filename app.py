import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# LOAD FILES
# -----------------------------
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Churn Prediction", layout="centered")

st.title("🍔 Food Delivery Churn Prediction")
st.write("Predict whether a customer is likely to churn")

# -----------------------------
# USER INPUTS
# -----------------------------
age = st.slider("Age", 18, 60, 25)
family_size = st.slider("Family Size", 1, 10, 3)

# Derived features
engagement = age * family_size
risk_score = age / (family_size + 1)

# -----------------------------
# CREATE INPUT DATAFRAME
# -----------------------------
input_data = pd.DataFrame(columns=features)

# Fill with zeros
input_data.loc[0] = 0

# Fill actual values
if "Age" in input_data.columns:
    input_data.at[0, "Age"] = age

if "Family size" in input_data.columns:
    input_data.at[0, "Family size"] = family_size

if "Engagement" in input_data.columns:
    input_data.at[0, "Engagement"] = engagement

if "Risk_Score" in input_data.columns:
    input_data.at[0, "Risk_Score"] = risk_score

# -----------------------------
# SCALE DATA
# -----------------------------
input_scaled = scaler.transform(input_data)

# -----------------------------
# PREDICT
# -----------------------------
prob = model.predict_proba(input_scaled)[0][1]

# -----------------------------
# OUTPUT
# -----------------------------
st.subheader("📊 Prediction Result")

st.write(f"### Churn Probability: {prob:.2f}")

if prob > 0.5:
    st.error("⚠️ High Risk Customer")
else:
    st.success("✅ Low Risk Customer")

# -----------------------------
# EXTRA INSIGHT
# -----------------------------
st.markdown("### 💡 Insight")
if prob > 0.5:
    st.write("This customer shows high risk of churn. Consider retention strategies.")
else:
    st.write("This customer is likely to stay engaged.")