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
