import pandas as pd

from app.database.mongodb import collection


def get_news_trends():

    articles = list(
        collection.find(
            {},
            {
                "_id": 0,
                "published": 1,
                "source": 1,
                "topic": 1,
                "sentiment": 1
            }
        )
    )

    if not articles:
        return pd.DataFrame()

    df = pd.DataFrame(articles)

    df["published"] = pd.to_datetime(
        df["published"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["published"]
    )

    df["date"] = df["published"].dt.date

    trends = (
        df.groupby("date")
        .size()
        .reset_index(name="article_count")
        .sort_values("date")
    )

    return trends


if __name__ == "__main__":

    trends = get_news_trends()

    print("\nNews Trends:")
    print(trends.to_string(index=False))