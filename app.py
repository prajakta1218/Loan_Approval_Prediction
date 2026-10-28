# Minimal Streamlit app for debugging
import streamlit as st

st.title("🏦 Loan Approval Predictor")
st.write("Testing if app loads...")

try:
    import pandas as pd
    st.success("✅ Pandas imported")
except Exception as e:
    st.error(f"❌ Pandas error: {e}")

try:
    import joblib
    st.success("✅ Joblib imported")
except Exception as e:
    st.error(f"❌ Joblib error: {e}")

try:
    import sklearn
    st.success("✅ Sklearn imported")
except Exception as e:
    st.error(f"❌ Sklearn error: {e}")

try:
    model = joblib.load("model.pkl")
    st.success("✅ Model loaded successfully!")
    st.write(f"Model type: {type(model)}")
except Exception as e:
    st.error(f"❌ Model loading error: {e}")

st.write("If you see this text, the app is working!")

# Show file listing
import os
st.write("Files in directory:")
st.write(os.listdir("."))
