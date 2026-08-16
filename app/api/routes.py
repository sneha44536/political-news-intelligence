from fastapi import APIRouter

from app.database.mongodb import collection


router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Political News Intelligence API is running"
    }


@router.get("/articles")
def get_articles():

    articles = list(
        collection.find(
            {},
            {"_id": 0}
        ).limit(50)
    )

    return {
        "count": len(articles),
        "articles": articles
    }


@router.get("/stats")
def get_stats():

    total_articles = collection.count_documents({})

    positive = collection.count_documents(
        {"sentiment": "Positive"}
    )

    negative = collection.count_documents(
        {"sentiment": "Negative"}
    )

    neutral = collection.count_documents(
        {"sentiment": "Neutral"}
    )

    return {
        "total_articles": total_articles,
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }