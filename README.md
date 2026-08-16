# 📄 Political News Intelligence using NLP, FastAPI, MongoDB & Streamlit

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AI](https://img.shields.io/badge/AI-Political%20Intelligence-purple?style=for-the-badge)

---

# 📌 Project Overview

The **Political News Intelligence System** is an AI-powered news analytics platform that automatically collects political news articles from multiple sources, processes them using Natural Language Processing (NLP), performs sentiment analysis and topic classification, stores the results in MongoDB, and displays insights through an interactive Streamlit dashboard.

The system combines **Web Scraping, Data Engineering, NLP, FastAPI, MongoDB, Docker, and Data Visualization** to create an end-to-end AI application.

This project demonstrates how AI can transform unstructured news data into actionable insights for media agencies, political analysts, researchers, and citizens.

---

# 🔗 Live Project

### 🌐 GitHub Repository:
https://github.com/sneha44536/political-news-intelligence

### 🚀 Streamlit Dashboard:
Add your deployed Streamlit URL here:

https://your-streamlit-url.streamlit.app

---

# 🚀 Problem Statement

Political news is generated continuously from multiple sources.

Challenges include:

- Huge amount of daily news articles
- Difficult to analyze public sentiment manually
- Time-consuming trend analysis
- No automatic topic categorization
- Hard to identify political patterns

👉 This project solves these problems by:

- Automatically collecting political news
- Cleaning and preprocessing text
- Performing sentiment analysis
- Identifying news topics
- Generating analytics dashboard
- Providing API access

---

# 📌 Objective

To build an AI-powered political news analytics system that automatically collects, processes, classifies, and visualizes political news using NLP and machine learning techniques.

---

# ⚙️ How the System Works

### Step 1: News Collection

News articles are collected from:

- Indian Express Politics
- Political Pulse
- Election News
- RSS Feeds

Libraries Used:

```python
requests
BeautifulSoup
feedparser
```

---

### Step 2: Data Cleaning

The collected data is cleaned by:

- Removing HTML tags
- Removing special characters
- Removing extra spaces
- Standardizing text

---

### Step 3: NLP Processing

News articles undergo:

- Sentiment Analysis
- Topic Classification
- Named Entity Recognition

---

### Step 4: Database Storage

Processed news is stored in:

```text
MongoDB
Database: political_news
Collection: articles
```

---

### Step 5: API Layer

FastAPI provides endpoints:

```text
/
 /stats
 /articles
 /topics
 /sentiment
```

---

### Step 6: Dashboard

Streamlit displays:

- Total Articles
- Sentiment Distribution
- Topic Distribution
- Latest News
- Trends

---

# 🧠 Why These Technologies Are Used

---

## 📌 BeautifulSoup

Used for web scraping.

### Why?

- Extracts article data from websites
- Parses HTML
- Lightweight and fast

---

## 📌 Requests Library

Used for HTTP requests.

### Why?

- Fetches webpage data
- Connects APIs

---

## 📌 NLP

Used for:

- Sentiment Analysis
- Topic Classification
- Text Processing

### Why?

Transforms text into meaningful insights.

---

## 📌 MongoDB

Used for database storage.

### Why?

- Flexible schema
- Stores JSON documents
- Suitable for news data

---

## 📌 FastAPI

Used to build APIs.

### Why?

- Fast
- Automatic documentation
- Easy integration

---

## 📌 Docker

Used for containerization.

### Why?

- Runs project anywhere
- Easy deployment
- Removes dependency issues

---

## 📌 Streamlit

Used for dashboard.

### Why?

- Easy frontend
- Interactive visualizations
- Quick deployment

---

# 🧠 NLP Techniques Used

---

## 📌 Sentiment Analysis

Classifies news into:

- Positive
- Negative
- Neutral

Example:

```text
"The government announced new policies"

Sentiment: Positive
```

---

## 📌 Topic Classification

Topics:

- Elections
- Economy
- Government
- Opposition
- Policies

Example:

```text
GDP Growth and Inflation

Topic: Economy
```

---

## 📌 Named Entity Recognition

Extracts:

- Person Names
- Political Parties
- Locations

Example:

```text
Narendra Modi → Person
BJP → Organization
Delhi → Location
```

---

# 📊 Dashboard Features

✅ Total Articles

✅ Sentiment Distribution

✅ Topic Analysis

✅ Latest News

✅ Political Trends

✅ Interactive Charts

---

# 📁 Project Structure

```text
political-news-intelligence/
│
├── app/
│   ├── analytics/
│   │   ├── political.py
│   │   └── trends.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── database/
│   │   └── mongodb.py
│   │
│   ├── nlp/
│   │   ├── sentiment.py
│   │   ├── entities.py
│   │   ├── topic.py
│   │   ├── topics.py
│   │   ├── update_sentiment.py
│   │   └── update_topics.py
│   │
│   ├── preprocessing/
│   │   └── cleaner.py
│   │
│   ├── scraper/
│   │   ├── rss_scraper.py
│   │   └── run_pipeline.py
│   │
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── processed/news.csv
│
├── logs/
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🔥 Key Features

✅ Automated News Collection

✅ NLP-Based Sentiment Analysis

✅ Topic Classification

✅ MongoDB Storage

✅ FastAPI Backend

✅ Streamlit Dashboard

✅ Docker Containerization

✅ GitHub Version Control

---

# 🌍 Applications

- Media Analytics
- Political Research
- Election Monitoring
- Public Opinion Analysis
- Government Policy Tracking
- Journalism

---

# 📈 Key Insights

- NLP converts text into intelligence
- MongoDB efficiently stores news data
- FastAPI provides scalable APIs
- Docker simplifies deployment
- Streamlit enables quick visualization

---

# 🚀 Future Improvements

- LLM-based News Summarization
- RAG Chatbot
- Real-Time News Alerts
- Political Forecasting
- Multi-language Support
- Cloud Deployment (AWS)

---

# 💻 API Endpoints

```text
GET /
GET /stats
GET /articles
GET /topics
GET /sentiment
```

---

# 🐳 Docker Commands

Build Image:

```bash
docker build -t political-news-intelligence .
```

Run Container:

```bash
docker run -d -p 8000:8000 political-news-intelligence
```

Check Logs:

```bash
docker logs political-news-app
```

---

# ▶️ Run Project

Backend:

```bash
uvicorn app.main:app --reload
```

Dashboard:

```bash
streamlit run dashboard/app.py
```

---

# 🧑‍💻 Author

### Sneha Jagannath Pise

B.Tech ENTC | AI/ML Enthusiast | Data Science | NLP | Generative AI

Skills Demonstrated:

- Python
- Web Scraping
- NLP
- MongoDB
- FastAPI
- Streamlit
- Docker
- GitHub
- API Development
- Data Engineering
- Data Visualization

---
