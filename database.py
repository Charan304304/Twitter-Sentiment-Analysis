

from pymongo import MongoClient

def insert_data(df):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["twitter_db"]
    collection = db["tweets"]

    records = df.head(1000).to_dict("records")
    collection.insert_many(records)

    print("Data inserted into MongoDB successfully!")