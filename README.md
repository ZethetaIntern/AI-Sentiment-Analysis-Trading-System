# 📈 AI Sentiment Analysis Trading System

## Overview

The AI Sentiment Analysis Trading System is a Python-based project that analyzes real-time financial news, extracts meaningful information, predicts market reactions, and generates automated trading signals.

The project combines Natural Language Processing (NLP), sentiment analysis, market reaction prediction, and live stock price data to simulate an intelligent news-driven trading assistant.

---

## Features

### ✅ Live Financial News Collection
- Fetches real-time financial news headlines
- Supports stock ticker search
- Processes multiple news articles automatically

### ✅ Named Entity Recognition (NER)
Extracts:

- Companies
- CEOs
- Important people

Example:

Headline:

Apple CEO Tim Cook announces major AI investment.

Output:

- Company: Apple
- Person: Tim Cook

---

### ✅ Sentiment Analysis

Analyzes every news headline and classifies it into:

- Positive
- Neutral
- Negative

Uses:

- FinBERT
- VADER Sentiment

---

### ✅ Event Classification

Automatically identifies financial events including:

- Earnings
- Mergers & Acquisitions
- Product Launch
- AI Investment
- Regulation
- Management Change
- Market Update
- General News

---

### ✅ Market Reaction Prediction

Predicts expected market movement based on:

- Sentiment
- Event Type
- News Impact

Example:

Positive Earnings

↓

Expected Price Move

+4%

---

### ✅ Trading Signal Generation

Automatically generates:

- BUY
- HOLD
- SELL

signals using market sentiment and expected price movement.

---

### ✅ Live Stock Price

Fetches:

- Current Price
- Previous Close
- Percentage Change

using Yahoo Finance.

---

### ✅ Master Report

Generates a complete CSV report containing:

- Stock Ticker
- Headline
- Companies
- Event Type
- Sentiment
- Market Reaction
- Expected Price Move
- Trading Signal
- Current Price
- Previous Close
- Percentage Change

Output:

```
data/master_report.csv
```

---

## Project Structure

```
AI-Sentiment-Analysis-Trading-System
│
├── data
│
├── outputs
│
├── notebooks
│
├── src
│   ├── main.py
│   ├── news_api.py
│   ├── sentiment.py
│   ├── finbert_sentiment.py
│   ├── ner.py
│   ├── event_classifier.py
│   ├── market_reaction.py
│   ├── stock_price.py
│   ├── trading.py
│   ├── dashboard.py
│   ├── visual_report.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Yahoo Finance API
- FinBERT
- VADER Sentiment
- NLP
- Machine Learning Concepts

---

## Workflow

Financial News

↓

Headline Parsing

↓

Named Entity Recognition

↓

Sentiment Analysis

↓

Event Classification

↓

Market Reaction Prediction

↓

Trading Signal Generation

↓

Live Stock Price

↓

Master Report

---

## Sample Output

| Headline | Sentiment | Event | Signal |
|----------|-----------|--------|--------|
| Apple beats earnings expectations | Positive | Earnings | BUY |
| Tesla recalls vehicles | Negative | Regulation | SELL |
| Microsoft announces AI partnership | Positive | AI Investment | BUY |

---

## Future Improvements

- GPT-powered news summarization
- Deep learning prediction models
- Real-time dashboard
- Portfolio optimization
- Risk scoring
- Backtesting engine
- Options strategy recommendation

---

## Author

**Om Pawar**

MBA Global (Finance)

University of South Wales

Investment Banking & Financial Analytics Enthusiast

GitHub:
https://github.com/omanant1104-alt

---

## Disclaimer

This project is developed for educational and internship purposes only.

It should not be considered financial or investment advice.