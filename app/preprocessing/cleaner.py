import re
import pandas as pd


def clean_text(text):

    if not text:
        return ""

    # Remove HTML tags
    text = re.sub(
        r"<[^>]+>",
        " ",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def clean_articles(articles):

    df = pd.DataFrame(articles)

    if df.empty:
        return df

    # Clean title
    df["title"] = df["title"].apply(
        clean_text
    )

    # Clean summary
    df["summary"] = df["summary"].apply(
        clean_text
    )

    # Remove rows without URL
    df = df[
        df["url"].notna()
        & (df["url"] != "")
    ]

    # Remove duplicate articles
    df = df.drop_duplicates(
        subset=["url"]
    )

    # Reset index
    df = df.reset_index(
        drop=True
    )

    return df