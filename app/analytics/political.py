from collections import Counter

from app.database.mongodb import collection
from app.nlp.entities import extract_entities


def get_political_analytics():

    articles = list(collection.find({}))

    people_counter = Counter()
    organization_counter = Counter()
    location_counter = Counter()
    topic_counter = Counter()
    sentiment_counter = Counter()

    for article in articles:

        title = article.get("title", "")
        summary = article.get("summary", "")

        text = f"{title} {summary}"

        entities = extract_entities(text)

        people_counter.update(entities["people"])
        organization_counter.update(entities["organizations"])
        location_counter.update(entities["locations"])

        topic = article.get("topic", "General Politics")
        sentiment = article.get("sentiment", "Neutral")

        topic_counter[topic] += 1
        sentiment_counter[sentiment] += 1

    return {
        "total_articles": len(articles),
        "top_people": people_counter.most_common(10),
        "top_organizations": organization_counter.most_common(10),
        "top_locations": location_counter.most_common(10),
        "topics": dict(topic_counter),
        "sentiments": dict(sentiment_counter)
    }


if __name__ == "__main__":

    analytics = get_political_analytics()

    print("\nTotal Articles:")
    print(analytics["total_articles"])

    print("\nTop People:")
    print(analytics["top_people"])

    print("\nTop Organizations:")
    print(analytics["top_organizations"])

    print("\nTop Locations:")
    print(analytics["top_locations"])

    print("\nTopics:")
    print(analytics["topics"])

    print("\nSentiments:")
    print(analytics["sentiments"])
    