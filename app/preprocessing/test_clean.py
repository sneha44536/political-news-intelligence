import json
import os

from app.preprocessing.cleaner import (
    clean_articles
)


with open(
    "data/raw/news.json",
    "r",
    encoding="utf-8"
) as f:

    articles = json.load(f)


df = clean_articles(articles)

os.makedirs(
    "data/processed",
    exist_ok=True
)

df.to_csv(
    "data/processed/news.csv",
    index=False
)

print(
    f"Saved {len(df)} clean articles."
)