
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

from app.scraper.rss_scraper import scrape_all
from app.preprocessing.cleaner import clean_articles
from app.database.mongodb import insert_articles
from app.nlp.update_sentiment import update_sentiment
from app.nlp.update_topics import update_topics


def run_pipeline():

    print("\n========== POLITICAL NEWS PIPELINE ==========\n")

    try:

        print("[1/5] Scraping articles...")

        articles = scrape_all()

        print(f"Scraped: {len(articles)} articles")

        print("\n[2/5] Cleaning articles...")

        df = clean_articles(articles)

        print(f"After cleaning: {len(df)} articles")

        print("\n[3/5] Storing articles in MongoDB...")

        clean_data = df.to_dict(orient="records")

        inserted = insert_articles(clean_data)

        print(f"New articles inserted: {inserted}")

        print("\n[4/5] Running sentiment analysis...")

        update_sentiment()

        print("\n[5/5] Classifying topics...")

        update_topics()

        print("\n========== PIPELINE COMPLETED ==========\n")

    except Exception as e:

        print("\nPIPELINE ERROR:")
        print(e)


if __name__ == "__main__":
    run_pipeline()