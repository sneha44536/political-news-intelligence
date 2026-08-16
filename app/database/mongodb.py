import os

from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://host.docker.internal:27017"
)

DATABASE_NAME = "political_news"

COLLECTION_NAME = "articles"


client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]


def insert_articles(articles):

    if not articles:
        return 0

    inserted = 0

    for article in articles:

        result = collection.update_one(
            {
                "url": article["url"]
            },
            {
                "$set": article
            },
            upsert=True
        )

        if result.upserted_id:
            inserted += 1

    return inserted


def get_articles():

    return list(
        collection.find(
            {},
            {"_id": 0}
        )
    )