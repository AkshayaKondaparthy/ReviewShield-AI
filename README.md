🛡️ ReviewShield AI

> AI-Powered Fake Review Detection & Review Authenticity Analysis



ReviewShield AI is an intelligent review-analysis platform designed to detect potentially fake or deceptive product reviews using Machine Learning and Natural Language Processing (NLP).

Instead of simply classifying a review as Fake or Genuine, ReviewShield AI provides an Authenticity Score, Confidence Score, Sentiment Analysis, Risk Level, and explainable insights to help users understand why a review may be suspicious.


---

🚀 Key Features

🔍 AI-Powered Fake Review Detection — Classifies reviews as Fake or Genuine.

🛡️ Authenticity Score — Provides a 0–100 score representing the estimated trustworthiness of a review.

📊 Confidence Score — Shows how confident the ML model is about its prediction.

💡 Explainable AI — Displays important factors contributing to the prediction.

😊 Sentiment Analysis — Analyzes the emotional tone of the review.

📈 Analytics Dashboard — Visualizes review patterns, predictions, ratings, and sentiments.

📄 Reports — Generate and download analysis results.

📁 Bulk Review Analysis — Analyze multiple reviews using CSV input.



---

🎯 Problem Statement

Fake Review Detection

Online reviews strongly influence purchasing decisions, but fake and coordinated reviews can manipulate ratings, mislead customers, and damage trust in e-commerce platforms.

ReviewShield AI addresses this problem by analyzing review text and behavioral/textual patterns to identify potentially deceptive reviews.


---

💡 Proposed Solution

ReviewShield AI combines NLP, Machine Learning, sentiment analysis, and feature engineering to evaluate reviews.

The system analyzes characteristics such as:

Review text

TF-IDF linguistic patterns

Review length

Word count

Rating

Repeated words

Capitalization patterns

Exclamation usage

Sentiment

Other engineered review characteristics


The extracted features are passed to a trained ML classifier to generate the final prediction.


---

🧠 Machine Learning Pipeline

Review
                       │
                       ▼
              Text Preprocessing
                       │
                       ▼
             Feature Engineering
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
       TF-IDF                Numerical Features
          │                         │
          └────────────┬────────────┘
                       ▼
              Feature Combination
                       │
                       ▼
             Logistic Regression
                       │
                       ▼
                 Prediction
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Fake/       Confidence    Authenticity
      Genuine        Score          Score
                       │
                       ▼
                Explainable AI


---

🔬 Model

The current implementation uses:

Algorithm: Logistic Regression

Text Representation: TF-IDF

Additional Features:

Review length

Word count

Rating

Helpful votes

Repeated words

Capital letters

Exclamation marks

Sentiment score


Model Serialization: Joblib


---

🛠️ Technology Stack

Frontend

React

Vite

Tailwind CSS

React Router

Axios

Recharts

Framer Motion


Backend

Python

FastAPI

Uvicorn

Pandas

NumPy

Scikit-learn

Joblib


Machine Learning

NLP

TF-IDF

Logistic Regression

VADER Sentiment Analysis

Feature Engineering


Deployment

Frontend: Vercel

Backend: Render


> No database is required. The application processes reviews through the API and loads the trained ML artifacts directly.




---

📁 Project Structure

ReviewShield-AI/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── components/
│       ├── pages/
│       │   ├── Landing.jsx
│       │   ├── Dashboard.jsx
│       │   ├── AnalyzeReview.jsx
│       │   ├── Analytics.jsx
│       │   ├── Reports.jsx
│       │   └── About.jsx
│       ├── services/
│       │   └── api.js
│       ├── routes/
│       ├── App.jsx
│       └── main.jsx
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── predict.py
│   │   │   ├── analytics.py
│   │   │   └── reports.py
│   │   ├── services/
│   │   │   ├── ml_service.py
│   │   │   ├── analytics_service.py
│   │   │   └── report_service.py
│   │   ├── utils/
│   │   │   ├── preprocessing.py
│   │   │   └── feature_engineering.py
│   │   ├── models/
│   │   │   ├── review_model.pkl
│   │   │   ├── tfidf_vectorizer.pkl
│   │   │   └── feature_scaler.pkl
│   │   └── main.py
│   └── requirements.txt
│
├── ml_model/
│   ├── notebooks/
│   ├── train.py
│   └── evaluate.py
│
├── datasets/
│   ├── raw/
│   ├── processed/
│   └── sample_reviews.csv
│
├── README.md
├── .gitignore
└── docker-compose.yml


---

🖥️ Application Pages

🏠 Landing

Introduces ReviewShield AI, its purpose, capabilities, workflow, and technology.

📊 Dashboard

Displays:

Total reviews analyzed

Fake reviews

Genuine reviews

Model statistics

Prediction overview

Recent analysis


🔍 Analyze Review

Users can enter a product review and receive:

Prediction:        FAKE
Confidence:        96%
Authenticity:      18/100
Risk Level:        HIGH
Sentiment:         Very Positive

The page also provides an explanation of the prediction.

📈 Analytics

Provides visual insights such as:

Fake vs Genuine distribution

Rating distribution

Sentiment distribution

Review-length patterns

Prediction statistics

Feature importance


📄 Reports

Allows users to view and export analysis results.

ℹ️ About

Contains:

Problem statement

Proposed solution

ML methodology

Technology stack

System architecture

Project information



---

🔗 API Endpoints

Method	Endpoint	Purpose

POST	/predict	Analyze a single review
POST	/bulk-predict	Analyze multiple reviews
GET	/analytics	Get analysis statistics
GET	/reports	Get generated reports
GET	/health	Check API status



---

⚙️ Installation

1. Clone the Repository

git clone <your-repository-url>
cd ReviewShield-AI

2. Backend Setup

cd backend

python -m venv venv

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Start FastAPI:

uvicorn app.main:app --reload

Backend:

http://localhost:8000

Swagger API documentation:

http://localhost:8000/docs


---

🎨 Frontend Setup

cd frontend
npm install
npm run dev

Frontend:

http://localhost:5173


---

📊 Dataset

The model is trained using a labeled review dataset containing review text and associated authenticity labels.

The preprocessing pipeline includes:

Raw Dataset
     ↓
Missing Value Handling
     ↓
Duplicate Removal
     ↓
Text Cleaning
     ↓
Feature Engineering
     ↓
Label Encoding
     ↓
Train/Test Split
     ↓
TF-IDF
     ↓
Model Training


---

📈 Evaluation Metrics

The model is evaluated using:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix


For fake-review detection, precision, recall, and F1-score are particularly important because both false accusations and missed fake reviews matter.


---

🔐 Responsible AI

ReviewShield AI is intended as a decision-support system, not a definitive authority on whether a person or review is fraudulent.

A prediction represents the model's assessment based on learned patterns and should be reviewed alongside other evidence.


---

🚀 Future Enhancements

🔄 Real-time review monitoring

🌐 Multilingual fake-review detection

🧠 Transformer-based models such as BERT

🔗 Product-level coordinated-review detection

👥 Reviewer behavior analysis

🕸️ Review/reviewer relationship graphs

⚡ Real-time e-commerce integration

🤖 Advanced LLM-based explanations



---

🏆 Project Goal

ReviewShield AI aims to make online reviews more trustworthy by combining machine learning, NLP, explainability, and intuitive visual analytics into a single platform.

> Detect. Explain. Protect. — ReviewShield AI