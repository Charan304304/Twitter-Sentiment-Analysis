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
