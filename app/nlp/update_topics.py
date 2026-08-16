from app.database.mongodb import collection
from app.nlp.topics import classify_topic


def update_topics():

    articles = collection.find({})

    updated = 0

    for article in articles:

        title = article.get("title", "")
        summary = article.get("summary", "")

        topic = classify_topic(
            title,
            summary
        )

        collection.update_one(
            {"_id": article["_id"]},
            {
                "$set": {
                    "topic": topic
                }
            }
        )

        updated += 1

    print("Topic classification completed.")
    print(f"Articles updated: {updated}")


if __name__ == "__main__":
    update_topics()