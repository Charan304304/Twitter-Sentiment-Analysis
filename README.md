# 🐦 Twitter Sentiment Analysis Web Application

## 📌 Overview
This project performs sentiment analysis on Twitter data using Machine Learning and MongoDB.  
It includes NLP preprocessing, TF-IDF feature engineering, Logistic Regression classification, model serialization, database integration, and a Streamlit web dashboard for real-time sentiment prediction.

The system follows a production-style ML workflow:
Train → Save Model → Load Model → Predict → Visualize → Store in Database

---

## 🚀 Features
- Text preprocessing using NLTK
- Stopword removal and text normalization
- TF-IDF vectorization
- Logistic Regression classifier
- ~77% model accuracy
- Model saved using Pickle
- MongoDB integration using PyMongo
- Real-time prediction via Streamlit
- Sentiment distribution visualization

---

## 🏗️ System Architecture

```mermaid
flowchart LR
    A[User Input - Streamlit UI] --> B[Text Preprocessing - NLTK]
    B --> C[TF-IDF Vectorization]
    C --> D[Logistic Regression Model]
    D --> E[Sentiment Prediction]
    D --> F[Model Saved - model.pkl]
    C --> G[MongoDB Database - twitter_db]

flowchart TD
    A[Raw Dataset - CSV] --> B[Load with Pandas]
    B --> C[Data Cleaning]
    C --> D[Remove Stopwords & Symbols]
    D --> E[TF-IDF Feature Extraction]
    E --> F[Train-Test Split]
    F --> G[Logistic Regression Training]
    G --> H[Model Evaluation - Accuracy]
    G --> I[Save Model using Pickle]

flowchart LR
    A[User Input Tweet] --> B[Clean Tweet Function]
    B --> C[Vectorizer Transform]
    C --> D[Loaded ML Model]
    D --> E[Sentiment Output]
    E --> F[Display in Streamlit]

flowchart TD
    A[Processed DataFrame] --> B[Convert to Dictionary]
    B --> C[PyMongo Client]
    C --> D[MongoDB Server]
    D --> E[Database: twitter_db]
    E --> F[Collection: tweets]

flowchart LR
    A[Local Machine] --> B[Python Environment]
    B --> C[Streamlit Application]
    C --> D[model.pkl + vectorizer.pkl]
    C --> E[MongoDB Server]
    C --> F[Web Browser - localhost:8501]

flowchart TD
    A[Twitter Dataset] --> B[Preprocessing - NLTK]
    B --> C[Feature Engineering - TF-IDF]
    C --> D[Model Training - Logistic Regression]
    D --> E[Model Serialization - Pickle]
    E --> F[Streamlit Web App]
    F --> G[Real-Time User Prediction]
    D --> H[MongoDB Storage]
```

