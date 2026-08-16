from app.database.mongodb import collection
from app.nlp.sentiment import analyze_sentiment


def update_sentiment():

    articles = collection.find()

    updated = 0

    for article in articles:

        text = (
            article.get("title", "")
            + " "
            + article.get("summary", "")
        )

        result = analyze_sentiment(text)

        collection.update_one(
            {"_id": article["_id"]},
            {
                "$set": {
                    "sentiment": result["label"],
                    "sentiment_score": result["score"]
                }
            }
        )

        updated += 1

    print("Sentiment analysis completed.")
    print(f"Articles updated: {updated}")


if __name__ == "__main__":
    update_sentiment()