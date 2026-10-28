# 🏦 Loan Approval Prediction – ML Model Deployment

A machine learning project for predicting loan approval using Random Forest Classifier, with interactive web interfaces built with Streamlit and Gradio.

## 📋 Project Structure

```
├── app.py              # Streamlit web interface
├── gradio_app.py       # Gradio web interface (enhanced)
├── train.py            # Model training script
├── model.pkl           # Trained Random Forest model
├── requirements.txt    # Python dependencies
├── README_HF.md        # Hugging Face Spaces README
├── DEPLOYMENT_GUIDE.md # Detailed deployment instructions
└── .gitignore         # Git ignore rules
```

## 🚀 Quick Start (Local)

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model**
   ```bash
   python train.py
   ```
   This creates `model.pkl` using loan.csv (if present) or synthetic data.

3. **Run the app**
   
   **Option A: Streamlit**
   ```bash
   streamlit run app.py
   ```
   Opens at: http://localhost:8501
   
   **Option B: Gradio (Enhanced UI)**
   ```bash
   python gradio_app.py
   ```
   Opens at: http://localhost:7860

## 🌐 Deployment Options

### 🤗 Hugging Face Spaces (Recommended)

**Quick Deploy:**
1. Create account at [huggingface.co](https://huggingface.co)
2. Create New Space → Select **Gradio** SDK
3. Upload files:
   - Rename `gradio_app.py` → `app.py`
   - Upload `model.pkl`, `requirements.txt`
   - Upload `README_HF.md` as `README.md`
4. Done! Your app is live 🎉

**Example URL:** `https://huggingface.co/spaces/YOUR_USERNAME/loan-approval-predictor`

### ☁️ Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" → Select your repo
4. Set main file as `app.py`
5. Deploy!

**Full instructions:** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## ✨ Features

### Streamlit App
- Clean, professional interface
- Real-time predictions
- Probability scores
- Mobile-responsive

### Gradio App (Enhanced)
- Modern, themed UI
- Slider inputs for better UX
- Example cases included
- Visual probability display
- Detailed result feedback

## 📊 Model Details

- **Algorithm:** Random Forest Classifier
- **Trees:** 300
- **Max Depth:** 8
- **Features:** 11 (personal, financial, property info)
- **Output:** Approval probability + binary decision

## 🛠️ Tech Stack

- **ML:** scikit-learn, pandas, numpy
- **UI:** Streamlit, Gradio
- **Deployment:** Hugging Face Spaces, Streamlit Cloud
- **Model:** joblib serialization

## 📖 Documentation

- **Deployment Guide:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **HF Spaces README:** [README_HF.md](README_HF.md)

## 🎓 Educational Purpose

This project is designed for learning ML model deployment. **Not for production loan decisions.**

## 📝 License

MIT License - Feel free to use for educational purposes!
