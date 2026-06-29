# AI-Powered Sentiment Analysis Trading System

## Overview

This project is an AI-powered trading system that analyzes financial news headlines using the FinBERT model and generates BUY, SELL, or HOLD trading signals based on market sentiment.

The application also retrieves live stock prices, creates visual reports, and provides an interactive dashboard using Streamlit.

---

## Features

- Collect financial news using NewsAPI
- Clean and preprocess news headlines
- Analyze sentiment using FinBERT
- Generate BUY, SELL, and HOLD trading signals
- Retrieve live stock prices
- Generate CSV reports
- Create visual charts
- Interactive Streamlit dashboard

---

## Technologies Used

- Python
- Pandas
- Requests
- Transformers (FinBERT)
- PyTorch
- Streamlit
- Matplotlib
- Plotly
- NewsAPI
- Finnhub API

---

## Project Structure

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
│   ├── finbert_sentiment.py
│   ├── news_api.py
│   ├── news_pipeline.py
│   ├── preprocess.py
│   ├── sentiment.py
│   ├── stock_price.py
│   ├── trading.py
│   ├── view_report.py
│   └── visual_report.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Go into the project folder:

```bash
cd Sentiment-Analysis-Trading
```

Install all required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Run the dashboard:

```bash
streamlit run src/dashboard.py
```

---

## Workflow

1. Fetch financial news
2. Clean the news headlines
3. Perform sentiment analysis using FinBERT
4. Generate trading signals
5. Retrieve stock prices
6. Generate reports
7. Display dashboard

---

## Output

The project generates:

- Trading signals
- Confidence scores
- CSV reports
- Interactive charts
- AI Trading Dashboard

---

## Future Improvements

- Portfolio optimization
- Email alerts
- Multiple stock comparison
- Real-time streaming data
- Risk analysis dashboard

---

## Author

Om Anant Pawar

MBA Global (Finance)

University of South Wales