# 🍔 Food Delivery Customer Churn Prediction

## 🚀 Live Demo

🔗 https://medhashree05-churn-prediction-app-9qagw8.streamlit.app/

---

## 📌 Overview

This project builds a **machine learning-based churn prediction system** for food delivery platforms.
It identifies customers who are likely to stop ordering and helps businesses take proactive retention actions.

The model is deployed as an interactive web application using **Streamlit**, enabling real-time predictions.

---

## 🎯 Objective

* Predict whether a customer will churn
* Identify key factors influencing churn
* Provide actionable insights for customer retention

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📊 Dataset

* Online Food Delivery Dataset (Kaggle)
* Includes:

  * Customer demographics (Age, Gender, Occupation)
  * Behavioral features (Family size, feedback, etc.)

---

## 🔍 Exploratory Data Analysis (EDA)

* Analyzed churn distribution
* Studied relationships between customer features and churn
* Visualized patterns using:

  * Count plots
  * Box plots
  * Heatmaps

---

## 🛠️ Feature Engineering

* Created new features:

  * **Engagement Score** = Age × Family size
  * **Risk Score** = Age / (Family size + 1)
  * **Age Groups** (Young, Adult, etc.)
* Improved model performance and interpretability

---

## 🤖 Model Building

* Logistic Regression (baseline)
* Random Forest (final model)

### ⚠️ Handling Imbalance

* Used `class_weight="balanced"` to improve churn prediction

---

## 📊 Model Evaluation

* Accuracy
* Precision / Recall
* Confusion Matrix

👉 Focus: **Recall for churn class (important for business impact)**

---

## 🔥 Feature Importance

* Identified top factors influencing churn:

  * Engagement
  * Age
  * Family size

---

## 🌐 Deployment

* Built interactive UI using Streamlit
* Users can input:

  * Age
  * Family size

👉 Output:

* Churn probability
* Risk level (High / Low)

Streamlit enables quick deployment of ML apps with minimal frontend effort ([Docker][1])

---

## 💡 Business Insights

* Low engagement users are more likely to churn
* Behavioral patterns strongly influence retention
* Early identification of churn improves revenue

---

## 🚀 Business Recommendations

* Target high-risk users with personalized offers
* Improve engagement strategies
* Retain high-value users through loyalty programs

---

## 📁 Project Structure

```
customer-churn-app/
│
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
```

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 Key Learnings

* End-to-end ML pipeline (EDA → Model → Deployment)
* Handling feature mismatch in production
* Building interactive ML apps using Streamlit
* Applying business-driven data science

---

## 👩‍💻 Author

**Medha Shree N**

[1]: https://www.docker.com/blog/how-to-develop-and-deploy-a-customer-churn-prediction-model-using-python-streamlit-and-docker/?utm_source=chatgpt.com "How to Develop and Deploy a Customer Churn Prediction ..."
