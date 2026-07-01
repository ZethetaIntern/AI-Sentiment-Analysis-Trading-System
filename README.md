# 📈 AI Sentiment Analysis Trading System

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![NLP](https://img.shields.io/badge/NLP-Financial%20News-green)
![FinBERT](https://img.shields.io/badge/Model-FinBERT-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

# 📖 Project Overview

This project is an AI-powered financial news sentiment analysis and trading recommendation system.

The system collects financial news headlines, analyzes their sentiment using **FinBERT** and **VADER**, extracts companies and people using **Named Entity Recognition (NER)**, classifies the type of market event, predicts the expected market reaction, and generates automated trading signals.

A professional **Streamlit Dashboard** visualizes the results, making it easy for analysts and investors to monitor market sentiment in real time.

---

# 🚀 Key Features

- ✅ Live Financial News Collection
- ✅ FinBERT Sentiment Analysis
- ✅ VADER Sentiment Analysis
- ✅ Named Entity Recognition (NER)
- ✅ News Event Classification
- ✅ Market Reaction Prediction
- ✅ Expected Price Movement Prediction
- ✅ Automated Trading Signal Generation
- ✅ Live Stock Price Integration
- ✅ Interactive Streamlit Dashboard
- ✅ CSV Report Generation

---

# 🏗️ System Architecture

```
Financial News API
        │
        ▼
Headline Parsing & Cleaning
        │
        ▼
Named Entity Recognition (NER)
        │
        ▼
FinBERT + VADER Sentiment Analysis
        │
        ▼
Event Classification
        │
        ▼
Market Reaction Prediction
        │
        ▼
Expected Price Movement
        │
        ▼
Trading Signal Generation
        │
        ▼
Streamlit Dashboard
        │
        ▼
CSV Report Generation
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Pandas | Data Processing |
| Streamlit | Interactive Dashboard |
| FinBERT | Financial Sentiment Analysis |
| VADER | Rule-Based Sentiment Analysis |
| Plotly | Interactive Charts |
| Yahoo Finance | Live Stock Prices |
| Git | Version Control |
| GitHub | Project Repository |

---

# 📂 Project Structure

```
Sentiment-Analysis-Trading/
│
├── api/
├── data/
├── models/
├── notebooks/
├── outputs/
├── src/
│   ├── dashboard.py
│   ├── event_classifier.py
│   ├── finbert_sentiment.py
│   ├── main.py
│   ├── market_reaction.py
│   ├── ner.py
│   ├── news_api.py
│   ├── pipeline.py
│   ├── preprocess.py
│   ├── sentiment.py
│   ├── stock_price.py
│   ├── trading.py
│   └── visual_report.py
│
├── test/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

- Live Stock Price
- Previous Closing Price
- Daily Percentage Change
- News Sentiment Summary
- Average AI Confidence
- BUY / HOLD / SELL Recommendation
- Trading Signal Distribution
- Sentiment Distribution
- Event Classification Charts
- Market Reaction Charts
- Confidence Score Visualization
- Detailed News Intelligence Panel

---

# 💹 Trading Strategy

The system generates trading recommendations based on:

- Overall Sentiment
- FinBERT Confidence Score
- Event Classification
- Expected Market Reaction
- Predicted Price Movement

Possible outputs include:

- 🟢 BUY
- 🟡 HOLD
- 🔴 SELL

---

# 📈 Sample Workflow

```
News Headline

↓

Sentiment Analysis

↓

Entity Recognition

↓

Event Classification

↓

Market Reaction Prediction

↓

Trading Signal

↓

Dashboard Visualization
```

---

# ▶️ How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the main pipeline:

```bash
python src/main.py
```

Launch the dashboard:

```bash
streamlit run src/dashboard.py
```

---

# 🎯 Future Improvements

- Large Language Model (LLM) Integration
- Multi-Stock Portfolio Analysis
- Real-Time News Streaming
- Deep Learning Price Prediction
- Risk Management Module
- Portfolio Optimization
- Email Alerts
- Cloud Deployment

---

# 👨‍💻 Author

**Om Anant Pawar**

MBA Global (Finance)  
University of South Wales

Investment Banking | Financial Analytics | AI in Finance

GitHub:
https://github.com/omanant1104-alt

---

# ⚠️ Disclaimer

This project was developed for educational and internship purposes.

The generated trading signals are AI-based predictions and should not be considered financial or investment advice.