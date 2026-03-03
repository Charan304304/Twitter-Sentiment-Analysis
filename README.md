# 🐦 Twitter Sentiment Analysis Web Application

## 📌 Overview
This project performs sentiment analysis on Twitter data using Machine Learning and MongoDB.  
It includes text preprocessing, model training, database storage, and a Streamlit web dashboard for real-time predictions.

---

## 🚀 Features
- Text preprocessing using NLTK
- TF-IDF feature extraction
- Logistic Regression classifier
- ~77% accuracy
- Model saved using Pickle
- MongoDB integration
- Real-time prediction with Streamlit
- Sentiment visualization

---

## 🏗️ System Architecture

```mermaid
flowchart LR
    A[Twitter Dataset] --> B[Text Preprocessing]
    B --> C[TF-IDF Vectorization]
    C --> D[Logistic Regression Model]
    D --> E[Save Model - Pickle]
    E --> F[Streamlit Web App]
    F --> G[User Prediction]
    D --> H[MongoDB Storage]
