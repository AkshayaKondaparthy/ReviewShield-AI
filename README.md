# 🛡️ ReviewShield AI

> **AI-Powered Fake Review Detection & Review Authenticity Analysis**

**Team:** Nexora  
**Project:** ReviewShield AI  
**Challenge:** Fake Review Detection

ReviewShield AI is an intelligent review-analysis platform that uses **Machine Learning, Natural Language Processing (NLP), sentiment analysis, and explainable AI** to identify potentially fake or deceptive product reviews.

Instead of simply classifying a review as **Fake** or **Genuine**, ReviewShield AI provides deeper insights including:

- 🛡️ Authenticity Score
- 🎯 Confidence Score
- 🚨 Risk Level
- 😊 Sentiment Analysis
- 💡 Explainable AI Insights
- 📊 Review Analytics
- 📄 Analysis Reports

> **Detect. Explain. Protect.**

---

## 🌐 Live Demo

### Frontend
https://review-shield-ai-uzle.vercel.app/

### Backend API
https://reviewshield-ai.onrender.com/

### API Documentation
https://reviewshield-ai.onrender.com/docs

---

# 🎯 Problem Statement

## Fake Review Detection

Online reviews have a major influence on purchasing decisions. However, fake, deceptive, and coordinated reviews can manipulate product ratings, mislead customers, and reduce trust in online marketplaces.

Traditional review systems often focus only on star ratings and basic moderation.

ReviewShield AI addresses this challenge by analyzing **linguistic, behavioral, rating, and sentiment-related patterns** to identify reviews that may exhibit suspicious characteristics.

---

# 💡 Proposed Solution

ReviewShield AI combines **NLP, Machine Learning, sentiment analysis, and feature engineering** to evaluate the authenticity of a review.

The system analyzes features such as:

- Review text
- TF-IDF linguistic patterns
- Review length
- Word count
- Rating
- Helpful votes
- Repeated words
- Capitalization patterns
- Exclamation usage
- Sentiment score
- Other engineered textual characteristics

These features are processed by a trained machine-learning model to generate a prediction.

The result is then transformed into an easy-to-understand **Review Health Report** containing prediction, confidence, authenticity, risk, sentiment, and explanation.

---

# 🚀 Key Features

### 🔍 AI-Powered Fake Review Detection

Classifies a submitted review as:

- **Fake**
- **Genuine**

---

### 🛡️ Authenticity Score

Provides a **0–100 authenticity score** representing the estimated trustworthiness of the review.

Higher scores indicate greater estimated authenticity.

---

### 🎯 Confidence Score

Displays the confidence of the machine-learning model in its prediction.

Example:

```text
Prediction: FAKE
Confidence: 96%
````

---

### 🚨 Risk Level

Reviews are categorized into risk levels based on the prediction and supporting signals.

```text
LOW
MEDIUM
HIGH
```

This provides a quick way for users to understand the potential risk associated with a review.

---

### 💡 Explainable AI

ReviewShield AI doesn't stop at prediction.

It provides understandable reasons behind suspicious classifications, such as:

* Excessive positive language
* Repeated words
* Excessive capitalization
* High exclamation usage
* Extreme ratings
* Unusual review patterns
* Sentiment characteristics

This makes the system more transparent and easier to interpret.

---

### 😊 Sentiment Analysis

Analyzes the emotional tone of the review and identifies sentiment characteristics such as:

* Positive
* Neutral
* Negative

---

### 📊 Analytics Dashboard

Provides visual insights into review patterns, including:

* Fake vs Genuine distribution
* Rating distribution
* Sentiment distribution
* Review-length patterns
* Prediction statistics
* Feature importance

---

### 📄 Reports

Users can view review-analysis results and generate reports containing important prediction information.

---

# 🧠 Machine Learning Pipeline

```text
                    REVIEW
                       │
                       ▼
              Text Preprocessing
                       │
                       ▼
             Feature Engineering
                       │
              ┌────────┴────────┐
              ▼                 ▼
            TF-IDF       Numerical Features
              │                 │
              └────────┬────────┘
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
       Fake/       Confidence   Authenticity
      Genuine        Score        Score
                       │
                       ▼
                Risk Assessment
                       │
                       ▼
                Explainable AI
```

---

# 🔬 Machine Learning Model

## Algorithm

**Logistic Regression**

Logistic Regression is used as the primary classification algorithm because it provides an efficient and interpretable approach for binary text classification.

## Text Representation

**TF-IDF (Term Frequency–Inverse Document Frequency)**

The review text is converted into numerical representations using TF-IDF features.

The implementation uses:

```text
max_features = 10000
ngram_range = (1, 2)
min_df = 2
sublinear_tf = True
```

## Additional Features

The model also incorporates numerical review characteristics such as:

* Review length
* Word count
* Review rating
* Helpful votes
* Repeated words
* Capital letters
* Uppercase ratio
* Exclamation marks
* Unique word count
* Average word length
* Sentiment score
* Review date characteristics
* Extreme rating indicator

## Model Serialization

The trained model and preprocessing components are serialized using:

**Joblib**

---

# 🛠️ Technology Stack

## Frontend

* React
* Vite
* Tailwind CSS
* React Router
* Axios
* Recharts
* Framer Motion
* Lucide React

## Backend

* Python
* FastAPI
* Uvicorn
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Machine Learning & NLP

* Natural Language Processing
* TF-IDF
* Logistic Regression
* VADER Sentiment Analysis
* Feature Engineering
* Explainable Prediction Logic

## Deployment

| Component         | Platform        |
| ----------------- | --------------- |
| Frontend          | Vercel          |
| Backend           | Render          |
| API Documentation | FastAPI Swagger |
| Database          | Not Required    |

> ReviewShield AI uses a **stateless API architecture** and does not require a traditional database for its core prediction workflow.

---

# 📁 Project Structure

```text
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
│       │
│       ├── services/
│       │   └── api.js
│       │
│       ├── routes/
│       │   └── AppRoutes.jsx
│       │
│       ├── App.jsx
│       └── main.jsx
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── predict.py
│   │   │   ├── analytics.py
│   │   │   └── reports.py
│   │   │
│   │   ├── services/
│   │   │   ├── ml_service.py
│   │   │   ├── analytics_service.py
│   │   │   └── report_service.py
│   │   │
│   │   ├── utils/
│   │   │   ├── preprocessing.py
│   │   │   └── feature_engineering.py
│   │   │
│   │   ├── models/
│   │   │   ├── review_model.pkl
│   │   │   ├── tfidf_vectorizer.pkl
│   │   │   └── feature_scaler.pkl
│   │   │
│   │   └── main.py
│   │
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
```

---

# 🖥️ Application Pages

ReviewShield AI consists of six primary application sections.

---

## 🏠 Landing Page

Introduces the ReviewShield AI platform.

Includes:

* Project overview
* Problem statement
* Key features
* AI workflow
* Technology stack
* Call-to-action
* Product highlights

---

## 📊 Dashboard

Provides a centralized overview of the review-analysis system.

Displays:

* Total reviews analyzed
* Fake reviews
* Genuine reviews
* Prediction statistics
* Review distribution
* Recent analysis
* Model-related insights

---

## 🔍 Analyze Review

The primary AI interaction page.

Users can enter a product review and optionally provide its rating.

The system returns information such as:

```text
Prediction:       FAKE
Confidence:       96%
Authenticity:     18/100
Risk Level:       HIGH
Sentiment:        Very Positive
```

The page also provides:

* AI explanation
* Suspicious patterns
* Feature analysis
* Sentiment information
* Authenticity assessment

---

## 📈 Analytics

Provides visual analysis of review patterns.

Includes:

* Fake vs Genuine distribution
* Rating distribution
* Sentiment distribution
* Review-length analysis
* Prediction statistics
* Feature importance

Charts are implemented using **Recharts**.

---

## 📄 Reports

Provides access to review-analysis results and report generation.

Reports can contain:

* Review information
* Prediction
* Confidence
* Authenticity score
* Risk level
* Sentiment
* Explanation
* Supporting analysis

---

## ℹ️ About

Provides information about:

* Problem statement
* Proposed solution
* Machine-learning methodology
* System architecture
* Technology stack
* Project objective
* Team information

---

# 🔗 API Endpoints

| Method | Endpoint        | Purpose                             |
| ------ | --------------- | ----------------------------------- |
| `POST` | `/predict`      | Analyze a single review             |
| `POST` | `/bulk-predict` | Analyze multiple reviews if enabled |
| `GET`  | `/analytics`    | Retrieve analysis statistics        |
| `GET`  | `/reports`      | Retrieve generated reports          |
| `GET`  | `/health`       | Check API availability              |

### API Documentation

FastAPI automatically provides interactive Swagger documentation:

```text
https://reviewshield-ai.onrender.com/docs
```

---

# ⚙️ Local Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd ReviewShield-AI
```

---

# 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# ⚛️ Frontend Setup

Open a new terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 📊 Dataset

The model is trained using a labeled product-review dataset containing review text and authenticity-related labels.

The preprocessing workflow includes:

```text
Raw Dataset
     │
     ▼
Missing Value Handling
     │
     ▼
Duplicate Removal
     │
     ▼
Text Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Label Processing
     │
     ▼
Train/Test Split
     │
     ▼
TF-IDF Transformation
     │
     ▼
Numerical Feature Scaling
     │
     ▼
Feature Combination
     │
     ▼
Model Training
```

---

# 📈 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

For fake-review detection, **Precision, Recall, and F1 Score** are especially important.

A false positive may incorrectly flag a genuine review, while a false negative may allow a deceptive review to pass through.

Therefore, the system should be treated as a **decision-support tool rather than an absolute fraud detector**.

---

# 🔐 Responsible AI

ReviewShield AI is designed as an **assistive review-analysis system**.

A prediction does not definitively prove that a review is fake or that a reviewer is fraudulent.

The model identifies patterns learned from the training data and estimates the likelihood that a review exhibits characteristics associated with fake reviews.

Users should consider:

* Model confidence
* Explanation signals
* Review context
* Product information
* Additional evidence

before making moderation or business decisions.

---

# 🚀 Future Enhancements

Potential future improvements include:

### 🌐 Multilingual Detection

Support fake-review detection across multiple languages.

### 🧠 Transformer Models

Explore advanced NLP architectures such as:

* BERT
* RoBERTa
* DistilBERT

### 🔗 Coordinated Review Detection

Identify groups of reviews that may be part of coordinated campaigns.

### 👥 Reviewer Behavior Analysis

Analyze reviewer-level behavioral patterns.

### 🕸️ Graph-Based Detection

Build review/reviewer/product relationship graphs to identify suspicious networks.

### ⚡ Real-Time Monitoring

Monitor incoming reviews continuously.

### 🛒 E-Commerce Integration

Integrate ReviewShield AI with e-commerce platforms and review-management systems.

### 🤖 Advanced AI Explanations

Use LLM-based explanations to provide more detailed and human-readable reasoning.

---

# 🏆 Project Goal

ReviewShield AI aims to improve trust in online reviews by combining:

**Machine Learning + NLP + Explainable AI + Visual Analytics**

into a single, intuitive platform.

The goal is not only to answer:

> **"Is this review fake?"**

but also:

> **"Why does the system consider this review suspicious?"**

This makes ReviewShield AI more transparent, useful, and actionable than a simple binary classifier.

---

# 👥 Team

## Nexora

Team Nexora focuses on building practical AI-powered solutions that transform real-world problems into intelligent, accessible, and impactful products.

---

# 📌 Project Information

| Item                | Details                |
| ------------------- | ---------------------- |
| Project Name        | ReviewShield AI        |
| Team                | Nexora                 |
| Challenge           | Fake Review Detection  |
| Domain              | Machine Learning / NLP |
| Frontend            | React + Vite           |
| Backend             | FastAPI                |
| ML Model            | Logistic Regression    |
| NLP                 | TF-IDF + VADER         |
| Frontend Deployment | Vercel                 |
| Backend Deployment  | Render                 |
| Database            | Not Required           |

---

# 🔗 Important Links

### 🌐 Live Application

[https://review-shield-ai-uzle.vercel.app/](https://review-shield-ai-uzle.vercel.app/)

### ⚙️ Backend API

[https://reviewshield-ai.onrender.com/](https://reviewshield-ai.onrender.com/)

### 📚 API Documentation

[https://reviewshield-ai.onrender.com/docs](https://reviewshield-ai.onrender.com/docs)

### 💻 GitHub

<your-github-repository-url>

---

# ⭐ ReviewShield AI

> **Detect. Explain. Protect.**

**Built by Team Nexora**

````

### One important change I recommend

Your current README says **“Bulk Review Analysis”** and includes `/bulk-predict`. If your deployed application **doesn't actually have bulk CSV functionality**, don't advertise it as a completed feature. Either remove it or label it as an optional/future feature.

Also, before submitting the hackathon form, replace:

```text
<your-github-repository-url>
````

with your actual GitHub repository URL.

Your submission should then have:

**Challenge:** `Fake Review Detection`

**Deployed Project:**
`https://review-shield-ai-uzle.vercel.app/`

**GitHub:** https://github.com/AkshayaKondaparthy/ReviewShield-AI

**Pitch Video:** https://drive.google.com/file/d/1O1QcgF3UX18f1XBOf0ICP-78VEGBtimL/view?usp=drivesdk

And the **Render backend URL stays inside the README/API documentation**, rather than being placed alongside the Vercel URL in the single deployment field.
