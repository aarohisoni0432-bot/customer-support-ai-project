import streamlit as st
import sys
import os

# IMPORTANT FIX (correct file)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.model import predict_text

st.set_page_config(page_title="Smart Support AI", page_icon="🤖", layout="centered")

# UI
st.title("🤖 Smart Support AI")
st.subheader("Customer Support Ticket Classifier")

user_input = st.text_area("✍️ Enter your issue:")

if st.button("🚀 Predict"):
    if user_input.strip() != "":
        result = predict_text(user_input)
        st.success(f"✅ Predicted Category: {result}")
    else:
        st.warning("⚠️ Please enter some text")