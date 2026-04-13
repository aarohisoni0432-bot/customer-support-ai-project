🤖 AI-Powered Customer Support Intelligence Platform

---

## 📌 Project Overview
This project builds an intelligent AI system to automate customer support operations using Machine Learning and Natural Language Processing (NLP).

The system analyzes customer support tickets and predicts key attributes to improve efficiency and decision-making.

---

## 🎯 Key Functionalities

🔹 Ticket Type Classification (NLP)
- Input: Ticket Subject + Description  
- Output: Billing / Technical / Product / Cancellation / Refund  
- Model: DistilBERT (Final Model)

🔹 Ticket Priority Prediction
- Output: Low / Medium / High / Critical  
- Based on structured features

🔹 Resolution Time Prediction
- Output: Time to resolve ticket (in hours)  
- Model: Regression

🔹 Customer Segmentation
- Model: K-Means Clustering  
- Groups customers based on behavior

---

## 🧠 Models Used

### 🔹 NLP Models
- TF-IDF + Naive Bayes
- Logistic Regression
- Random Forest
- ✅ DistilBERT (Final Model)

### 🔹 Regression Models
- Linear Regression

### 🔹 Clustering
- K-Means Clustering

---

## 📊 Project Workflow

1️⃣ Data Cleaning & Preprocessing  
2️⃣ Exploratory Data Analysis (EDA)  
3️⃣ Text Processing (NLP Pipeline)  
4️⃣ Baseline Model Building  
5️⃣ Advanced ML Models  
6️⃣ Deep Learning (BiLSTM)  
7️⃣ Transformer Model (DistilBERT)  
8️⃣ Regression + Clustering  
9️⃣ Explainability (SHAP)  
🔟 Deployment (FastAPI + Dashboard)

---

## 📂 Project Structure
customer-support-ai-project/ │ ├── app/                # FastAPI app & UI ├── models/             # Saved ML models ├── notebooks/          # Colab notebooks (Day 1–8) ├── report/             # Final HTML report ├── requirements.txt    # Dependencies

---

## 📈 Key Insights

- Dataset is balanced across ticket types and priorities  
- Model accuracy is limited due to synthetic data patterns  
- DistilBERT improves contextual understanding of text  
- Most tickets are resolved within 0–10 hours  
- Multi-channel customer interaction observed  

---

## ⚙️ Tools & Technologies

- Python  
- Scikit-learn  
- Transformers (Hugging Face)  
- PyTorch  
- FastAPI  
- SHAP  
- Matplotlib / Seaborn  

---

## 🚀 How to Run

`bash
pip install -r requirements.txt
python app/app_ui.py
📊 Features
✔ End-to-End ML Pipeline
✔ NLP + ML + Deep Learning
✔ Model Explainability (SHAP)
✔ Dashboard Visualization
✔ FastAPI Deployment
📌 Conclusion
This project demonstrates a complete AI-powered system for customer support automation, including data processing, model building, explainability, and deployment.
👩‍💻 Author
Aarohi Soni
