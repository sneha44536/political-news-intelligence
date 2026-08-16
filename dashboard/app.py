import requests
import pandas as pd
import streamlit as st
import plotly.express as px


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Political News Intelligence",
    page_icon="🇮🇳",
    layout="wide"
)


st.title(
    "🇮🇳 Political News Intelligence"
)

st.write(
    "News collection, sentiment and topic analysis"
)


# -------------------------
# Get statistics
# -------------------------

stats_response = requests.get(
    f"{API_URL}/stats"
)

stats = stats_response.json()


# -------------------------
# KPI cards
# -------------------------

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Articles",
    stats["total_articles"]
)

col2.metric(
    "Positive",
    stats["positive"]
)

col3.metric(
    "Negative",
    stats["negative"]
)

col4.metric(
    "Neutral",
    stats["neutral"]
)


st.divider()


# -------------------------
# Get articles
# -------------------------

response = requests.get(
    f"{API_URL}/articles"
)

articles = response.json()["articles"]

df = pd.DataFrame(articles)


if not df.empty:

    # -------------------------
    # Sentiment chart
    # -------------------------

    sentiment_counts = (
        df["sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_counts.columns = [
        "sentiment",
        "count"
    ]


    fig = px.pie(
        sentiment_counts,
        names="sentiment",
        values="count",
        title="Sentiment Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -------------------------
    # Topic chart
    # -------------------------

    topic_counts = (
        df["topic"]
        .value_counts()
        .reset_index()
    )

    topic_counts.columns = [
        "topic",
        "count"
    ]


    fig2 = px.bar(
        topic_counts,
        x="topic",
        y="count",
        title="Political Topics"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )


    # -------------------------
    # News table
    # -------------------------

    st.subheader(
        "Latest Political News"
    )


    display_columns = [
        "title",
        "source",
        "topic",
        "sentiment",
        "url"
    ]


    st.dataframe(
        df[display_columns],
        use_container_width=True
    )