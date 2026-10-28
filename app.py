# Streamlit app - Simple version for deployment
import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="wide")

# Title
st.title("🏦 Loan Approval Prediction System")
st.write("Machine Learning Model | Random Forest Classifier")

# Load model
@st.cache_resource
def load_model():
    try:
        return joblib.load("model.pkl")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is None:
    st.stop()

# Create tabs
tab1, tab2, tab3 = st.tabs(["📝 Prediction", "ℹ️ About", "📊 Model Info"])

with tab1:
    st.header("Enter Applicant Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Personal Information")
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Marital Status", ["Yes", "No"])
        dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        self_emp = st.selectbox("Self Employed", ["No", "Yes"])
        
    with col2:
        st.subheader("Financial Information")
        inc = st.slider("Applicant Income (monthly $)", 0, 50000, 5000, 500)
        coinc = st.slider("Coapplicant Income (monthly $)", 0, 50000, 0, 500)
        amt = st.slider("Loan Amount (in thousands $)", 10, 500, 130, 10)
        term = st.selectbox("Loan Term (months)", [120, 180, 240, 300, 360, 480], index=4)
        credit = st.radio("Credit History", [1, 0], format_func=lambda x: "Good (1)" if x == 1 else "Bad (0)", horizontal=True)
    
    st.subheader("Property Information")
    area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    
    st.markdown("---")
    
    if st.button("🔍 Predict Loan Approval", type="primary", use_container_width=True):
        try:
            # Create input dataframe
            row = pd.DataFrame([{
                "Gender": gender,
                "Married": married,
                "Dependents": dependents,
                "Education": education,
                "Self_Employed": self_emp,
                "Property_Area": area,
                "ApplicantIncome": inc,
                "CoapplicantIncome": coinc,
                "LoanAmount": amt,
                "Loan_Amount_Term": term,
                "Credit_History": credit
            }])
            
            # Make prediction
            pred = model.predict(row)[0]
            prob = model.predict_proba(row)[0][list(model.classes_).index("Y")]
            
            st.markdown("---")
            st.subheader("Prediction Results")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                if pred == "Y":
                    st.success("### ✅ LOAN APPROVED")
                    st.balloons()
                else:
                    st.error("### ❌ LOAN NOT APPROVED")
            
            with col_res2:
                st.metric("Approval Probability", f"{prob:.1%}")
            
            # Progress bar
            st.progress(prob)
            
            # Additional insights
            if prob > 0.7:
                st.info("💡 **Strong application** - High probability of approval")
            elif prob > 0.5:
                st.warning("💡 **Moderate application** - Consider improving credit history or income")
            else:
                st.error("💡 **Weak application** - May need to improve financial standing")
                
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

with tab2:
    st.markdown("""
    ### 📖 About This Application
    
    This is a **Machine Learning-powered Loan Approval Prediction System** that helps assess 
    loan application viability based on applicant information.
    
    #### How It Works:
    1. Enter applicant's personal and financial details
    2. Click "Predict Loan Approval"
    3. Get instant prediction with probability score
    
    #### Features Considered:
    - **Personal**: Gender, Marital Status, Dependents, Education, Employment
    - **Financial**: Applicant Income, Coapplicant Income, Loan Amount, Loan Term, Credit History
    - **Property**: Property Location (Urban/Semiurban/Rural)
    
    #### ⚠️ Important Notice:
    This is an **educational demonstration** of ML model deployment. It should **NOT** be used 
    for actual loan approval decisions.
    """)

with tab3:
    st.markdown("""
    ### 🤖 Model Technical Details
    
    **Algorithm:** Random Forest Classifier
    - **Number of Trees:** 300
    - **Max Depth:** 8
    - **Random State:** 42 (for reproducibility)
    
    **Training Data:**
    - Uses loan dataset with preprocessing
    - Features are encoded and normalized
    - Handles missing values automatically
    
    **Tech Stack:**
    - scikit-learn for ML
    - Streamlit for UI
    - Pandas for data manipulation
    - Joblib for model serialization
    """)
    
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit & scikit-learn")
