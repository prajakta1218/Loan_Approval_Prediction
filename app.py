import streamlit as st

st.write("# 🏦 Loan Approval Predictor")
st.write("App is loading...")

# Test 1: Check imports
st.write("## Testing Imports")

try:
    import pandas as pd
    st.write("✅ Pandas OK")
except Exception as e:
    st.write(f"❌ Pandas ERROR: {e}")

try:
    import joblib
    st.write("✅ Joblib OK")
except Exception as e:
    st.write(f"❌ Joblib ERROR: {e}")

try:
    import sklearn
    st.write(f"✅ Sklearn OK (version: {sklearn.__version__})")
except Exception as e:
    st.write(f"❌ Sklearn ERROR: {e}")

# Test 2: Check for model file
st.write("## Testing Model File")
import os
files = os.listdir(".")
st.write(f"Files found: {files}")

if "model.pkl" in files:
    st.write("✅ model.pkl exists")
    try:
        model = joblib.load("model.pkl")
        st.write(f"✅ Model loaded! Type: {type(model)}")
    except Exception as e:
        st.write(f"❌ Model load ERROR: {e}")
else:
    st.write("❌ model.pkl NOT FOUND")

st.write("---")
st.write("If you see this message, the app is working!")
