# Twitter Sentiment Analysis Project

## 📌 Overview
This project performs sentiment analysis on Twitter data using Machine Learning and MongoDB.

## 🚀 Features
- Data preprocessing using NLTK
- TF-IDF vectorization
- Logistic Regression classifier
- 77% model accuracy
- MongoDB integration
- Real-time sentiment prediction
- Sentiment distribution visualization

 ## 🏗️ System Architecture

```mermaid
flowchart LR
    A[User Input - Streamlit UI] --> B[Text Preprocessing - NLTK]
    B --> C[TF-IDF Vectorization]
    C --> D[Logistic Regression Model]
    D --> E[Sentiment Prediction]

    D --> F[Model Saved as model.pkl]
    F --> A

    C --> G[MongoDB Database]


This shows overall system structure.

---

# 🔄 2️⃣ MACHINE LEARNING PIPELINE FLOW

```markdown
## 🔄 Machine Learning Pipeline

```mermaid
flowchart TD
    A[Raw Twitter Dataset CSV] --> B[Data Cleaning]
    B --> C[Remove Stopwords & Symbols]
    C --> D[TF-IDF Feature Extraction]
    D --> E[Train-Test Split]
    E --> F[Logistic Regression Training]
    F --> G[Model Evaluation - Accuracy]
    F --> H[Save Model using Pickle]


---

# 📊 3️⃣ DATA FLOW DIAGRAM

```markdown
## 📊 Data Flow Diagram

```mermaid
flowchart LR
    User --> StreamlitApp
    StreamlitApp --> CleanTweetFunction
    CleanTweetFunction --> Vectorizer
    Vectorizer --> MLModel
    MLModel --> PredictionResult
    PredictionResult --> User

---

# 🗄️ 4️⃣ MongoDB Integration Flow

```markdown
## 🗄️ MongoDB Integration Flow

```mermaid
flowchart TD
    A[Processed DataFrame] --> B[Convert to Dictionary]
    B --> C[PyMongo Connection]
    C --> D[MongoDB Database - twitter_db]
    D --> E[Collection - tweets]


---

# 🌐 5️⃣ Deployment Architecture

```markdown
## 🌐 Deployment Architecture

```mermaid
flowchart LR
    A[Local Machine] --> B[Streamlit App]
    B --> C[Saved Model - model.pkl]
    C --> B
    B --> D[Web Browser - localhost:8501]

## 🛠 Technologies Used
- Python
- Pandas
- Scikit-learn
- NLTK
- MongoDB
- Matplotlib

## 📊 Model Performance
Accuracy: ~77%

## 💾 Database
Data stored in MongoDB using PyMongo.

## ▶ How To Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python main.py
