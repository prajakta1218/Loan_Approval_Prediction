# 🏦 Loan Approval Prediction

Machine Learning web app for predicting loan approval using Random Forest Classifier.

## 🚀 Quick Start

### Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens at: http://localhost:8501

## 📦 Project Files

- `app.py` - Streamlit web interface (currently in debug mode)
- `model.pkl` - Trained Random Forest model
- `train.py` - Model training script
- `requirements.txt` - Python dependencies

## 🌐 Deploy to Streamlit Cloud

1. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/loan-approval-predictor.git
   git push origin main
   ```

2. **Deploy:**
   - Go to: https://share.streamlit.io
   - Click "New app"
   - Select your repo
   - Main file: `app.py`
   - Deploy!

## 🔧 Current Status

The app is in **debug mode** to identify deployment issues. 

After pushing to GitHub and deploying to Streamlit Cloud, the app will show diagnostic messages to help troubleshoot any problems.

## 📊 Model Details

- **Algorithm:** Random Forest Classifier
- **Features:** Personal info, financial data, property details
- **Output:** Loan approval prediction with probability

## 🛠️ Tech Stack

- Python 3.9+
- Streamlit
- scikit-learn
- pandas
- joblib

## 📝 License

MIT License - Educational purposes
