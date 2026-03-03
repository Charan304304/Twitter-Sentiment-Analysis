
import streamlit as st
import pandas as pd
import pickle
from preprocessing import clean_tweet


@st.cache_resource
def load_saved_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

model, vectorizer = load_saved_model()


st.title("🐦 Twitter Sentiment Analysis Web App")
st.write("Enter a tweet to analyze its sentiment.")


user_input = st.text_area("Type your tweet here:")

if st.button("Predict Sentiment"):

    if user_input:
        cleaned = clean_tweet(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.success("Sentiment: Positive 😊")
        else:
            st.error("Sentiment: Negative 😠")
    else:
        st.warning("Please enter a tweet!")


@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/training.1600000.processed.noemoticon.csv",
        encoding="latin-1",
        header=None
    )
    df.columns = ["sentiment", "id", "date", "flag", "user", "text"]
    df = df[["sentiment", "text"]]
    df["sentiment"] = df["sentiment"].replace(4, 1)
    df = df.sample(10000)
    return df

df = load_data()

st.subheader("Sentiment Distribution in Dataset")
sentiment_counts = df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)