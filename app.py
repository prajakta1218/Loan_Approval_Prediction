import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Header
st.title("🏦 Loan Approval Prediction System")
st.markdown("**Machine Learning Model** | Random Forest Classifier")
st.markdown("---")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📝 Make Prediction", "ℹ️ About", "📊 Model Info"])

with tab1:
    st.header("Enter Applicant Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👤 Personal Information")
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Marital Status", ["Yes", "No"])
        dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["No", "Yes"])
        
    with col2:
        st.subheader("💰 Financial Information")
        applicant_income = st.slider("Applicant Income (monthly $)", 0, 50000, 5000, 500)
        coapplicant_income = st.slider("Coapplicant Income (monthly $)", 0, 50000, 0, 500)
        loan_amount = st.slider("Loan Amount (in thousands $)", 10, 500, 130, 10)
        loan_term = st.selectbox("Loan Term (months)", [120, 180, 240, 300, 360, 480], index=4)
        credit_history = st.radio("Credit History", [1, 0], format_func=lambda x: "✅ Good (1)" if x == 1 else "❌ Bad (0)", horizontal=True)
    
    st.subheader("🏘️ Property Information")
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    
    st.markdown("---")
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        predict_button = st.button("🔍 Predict Loan Approval", type="primary", use_container_width=True)
    
    if predict_button:
        with st.spinner("Analyzing application..."):
            # Create input dataframe
            input_data = pd.DataFrame([{
                "Gender": gender,
                "Married": married,
                "Dependents": dependents,
                "Education": education,
                "Self_Employed": self_employed,
                "Property_Area": property_area,
                "ApplicantIncome": applicant_income,
                "CoapplicantIncome": coapplicant_income,
                "LoanAmount": loan_amount,
                "Loan_Amount_Term": loan_term,
                "Credit_History": credit_history
            }])
            
            # Make prediction
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][list(model.classes_).index("Y")]
            
            st.markdown("---")
            st.subheader("📊 Prediction Results")
            
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                if prediction == "Y":
                    st.success("### ✅ LOAN APPROVED")
                    st.balloons()
                else:
                    st.error("### ❌ LOAN NOT APPROVED")
            
            with col_res2:
                st.metric("Approval Probability", f"{probability:.1%}")
            
            # Progress bar
            st.progress(probability)
            
            # Insights
            st.markdown("---")
            st.subheader("💡 Insights")
            
            if probability > 0.75:
                st.success("**Strong Application** - High probability of approval. Your financial profile looks excellent!")
            elif probability > 0.5:
                st.warning("**Moderate Application** - Consider improving your credit history or increasing income to boost approval chances.")
            else:
                st.error("**Weak Application** - You may need to improve your financial standing before applying.")
            
            # Show input summary
            with st.expander("📋 View Application Summary"):
                summary_col1, summary_col2 = st.columns(2)
                with summary_col1:
                    st.write("**Personal Details:**")
                    st.write(f"- Gender: {gender}")
                    st.write(f"- Married: {married}")
                    st.write(f"- Dependents: {dependents}")
                    st.write(f"- Education: {education}")
                    st.write(f"- Self Employed: {self_employed}")
                with summary_col2:
                    st.write("**Financial Details:**")
                    st.write(f"- Applicant Income: ${applicant_income:,}")
                    st.write(f"- Coapplicant Income: ${coapplicant_income:,}")
                    st.write(f"- Loan Amount: ${loan_amount * 1000:,}")
                    st.write(f"- Loan Term: {loan_term} months")
                    st.write(f"- Credit History: {'Good' if credit_history == 1 else 'Bad'}")
                    st.write(f"- Property Area: {property_area}")

with tab2:
    st.markdown("""
    ## 📖 About This Application
    
    This is a **Machine Learning-powered Loan Approval Prediction System** that helps assess 
    loan application viability based on applicant information.
    
    ### How It Works:
    1. **Enter Details**: Fill in the applicant's personal, financial, and property information
    2. **Click Predict**: The ML model analyzes the data
    3. **Get Results**: Receive instant prediction with probability score and insights
    
    ### Features Considered:
    
    **Personal Information:**
    - Gender, Marital Status, Number of Dependents
    - Education Level, Employment Type
    
    **Financial Information:**
    - Applicant Monthly Income
    - Coapplicant Monthly Income
    - Requested Loan Amount
    - Loan Term Duration
    - Credit History (Good/Bad)
    
    **Property Information:**
    - Property Location (Urban/Semiurban/Rural)
    
    ### ⚠️ Important Disclaimer:
    
    This is an **educational demonstration** of machine learning model deployment. 
    
    **This tool should NOT be used for actual loan approval decisions.** Real loan 
    decisions require comprehensive assessment by qualified financial professionals 
    and must comply with lending regulations and fair lending practices.
    
    ### 🎓 Educational Purpose:
    
    This project demonstrates:
    - Machine Learning classification
    - Model deployment with Streamlit
    - Interactive web application development
    - Real-time prediction serving
    """)

with tab3:
    st.markdown("""
    ## 🤖 Model Technical Details
    
    ### Algorithm: Random Forest Classifier
    
    **Model Parameters:**
    - Number of Trees: 300
    - Max Depth: 8
    - Random State: 42 (for reproducibility)
    
    ### Training Process:
    
    **Data Preprocessing:**
    - Categorical features encoded using One-Hot Encoding
    - Missing values handled automatically
    - Feature scaling applied where necessary
    
    **Features Used (11 total):**
    - 6 Categorical: Gender, Married, Dependents, Education, Self_Employed, Property_Area
    - 5 Numerical: ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History
    
    ### Model Performance:
    
    The model achieves strong predictive performance on the training dataset:
    - High accuracy in distinguishing approved vs. rejected applications
    - Balanced precision and recall
    - Robust to various input combinations
    
    ### Tech Stack:
    
    **Machine Learning:**
    - scikit-learn - Model training and pipeline
    - pandas - Data manipulation
    - numpy - Numerical operations
    
    **Web Application:**
    - Streamlit - Interactive UI framework
    - Python 3.9+ - Programming language
    
    **Model Deployment:**
    - joblib - Model serialization
    - Streamlit Cloud - Hosting platform
    
    ### Pipeline Architecture:
    
    ```
    Input Data
        ↓
    Preprocessing (One-Hot Encoding)
        ↓
    Random Forest Classifier
        ↓
    Prediction (Approved/Rejected)
        ↓
    Probability Score
    ```
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>Made with ❤️ using Streamlit & scikit-learn</p>
        <p>Machine Learning Model Deployment Demo</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📌 Quick Info")
    st.info("Fill in the applicant details in the 'Make Prediction' tab and click the predict button to get results.")
    
    st.markdown("---")
    st.subheader("📊 Model Status")
    st.success("✅ Model Loaded")
    st.success("✅ Ready for Predictions")
    
    st.markdown("---")
    st.subheader("🎯 Sample Scenarios")
    
    with st.expander("Strong Applicant"):
        st.write("- Income: $8000+")
        st.write("- Good Credit History")
        st.write("- Graduate")
        st.write("- Moderate Loan Amount")
    
    with st.expander("Weak Applicant"):
        st.write("- Low Income")
        st.write("- Bad Credit History")
        st.write("- High Loan Amount")
        st.write("- Not Graduate")
    
    st.markdown("---")
    st.caption("Educational Project | Not for Production Use")
