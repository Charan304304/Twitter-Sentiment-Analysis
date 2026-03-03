import pandas as pd


df = pd.read_csv(
    "data/training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None
)

df.columns = ["sentiment", "id", "date", "flag", "user", "text"]


df = df[["sentiment", "text"]]


df["sentiment"] = df["sentiment"].replace(4, 1)

print("Dataset Loaded Successfully!")
print(df.head())

import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_tweet(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


df["clean_text"] = df["text"].apply(clean_tweet)

print("Cleaning Done!")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["sentiment"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)


import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model saved successfully!")

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_db"]
collection = db["tweets"]


records = df.head(1000).to_dict("records")
collection.insert_many(records)

print("Data inserted into MongoDB!")

import matplotlib.pyplot as plt

sentiment_counts = df["sentiment"].value_counts()

plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.xlabel("Sentiment (0=Negative, 1=Positive)")
plt.ylabel("Count")
plt.title("Sentiment Distribution")
plt.show()


while True:
    user_input = input("\nEnter a tweet (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        break

    cleaned = clean_tweet(user_input)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)

    if prediction[0] == 1:
        print("Sentiment: Positive 😊")
    else:
        print("Sentiment: Negative 😠")