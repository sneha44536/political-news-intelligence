from app.scraper.rss_scraper import scrape_all
from app.preprocessing.cleaner import clean_articles
from app.database.mongodb import insert_articles


def run_pipeline():

    print("Starting scraper...")

    articles = scrape_all()

    print(
        f"Scraped {len(articles)} articles."
    )

    df = clean_articles(articles)

    clean_data = df.to_dict(
        orient="records"
    )

    inserted = insert_articles(
        clean_data
    )

    print(
        f"New articles inserted: {inserted}"
    )


if __name__ == "__main__":

    run_pipeline()