import feedparser
import json
import os
from datetime import datetime


FEEDS = {
    "Indian Express Politics":
        "https://indianexpress.com/section/politics/feed/",

    "Indian Express Political Pulse":
        "https://indianexpress.com/section/political-pulse/feed/",

    "Indian Express Elections":
        "https://indianexpress.com/elections/feed/",
}


def scrape_feed(source, url):

    print(f"Scraping: {source}")

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:

        article = {
            "title": entry.get("title", "").strip(),
            "url": entry.get("link", "").strip(),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
            "source": source,
            "scraped_at": datetime.utcnow()
        }

        articles.append(article)

    return articles


def scrape_all():

    all_articles = []

    for source, url in FEEDS.items():

        try:
            articles = scrape_feed(source, url)
            all_articles.extend(articles)

            print(
                f"{source}: "
                f"{len(articles)} articles"
            )

        except Exception as e:

            print(
                f"Error scraping {source}: {e}"
            )

    return all_articles


if __name__ == "__main__":

    articles = scrape_all()

    print("\nTotal articles:", len(articles))

    for article in articles[:5]:

        print("\nTitle:", article["title"])
        print("URL:", article["url"])
if __name__ == "__main__":

    articles = scrape_all()

    os.makedirs("data/raw", exist_ok=True)

    with open(
        "data/raw/news.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            articles,
            f,
            ensure_ascii=False,
            indent=4,
            default=str
        )

    print(
        f"\nSaved {len(articles)} articles."
    )