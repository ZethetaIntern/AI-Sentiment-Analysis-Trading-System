from news_api import fetch_company_news
from stock_price import get_stock_price
from preprocess import TextCleaner
from finbert_sentiment import FinBERTSentimentAnalyzer
import pandas as pd


def generate_signal(sentiment):
    if sentiment == "POSITIVE":
        return "BUY"
    elif sentiment == "NEGATIVE":
        return "SELL"
    else:
        return "HOLD"


ticker = input("Enter stock ticker: ").upper()

print("\nDownloading real financial news...")
news = fetch_company_news(ticker)

print("Getting stock price...")
price_data = get_stock_price(ticker)

cleaner = TextCleaner()
analyzer = FinBERTSentimentAnalyzer()

results = []

for item in news[:10]:
    headline = item.get("headline", "")
    cleaned = cleaner.clean(str(headline))
    sentiment_result = analyzer.analyze(cleaned)

    sentiment = sentiment_result["sentiment"]
    confidence = sentiment_result["confidence"]
    signal = generate_signal(sentiment)

    results.append({
        "ticker": ticker,
        "headline": headline,
        "cleaned_headline": cleaned,
        "sentiment": sentiment,
        "confidence": confidence,
        "trading_signal": signal,
        "current_price": price_data["current_price"],
        "previous_close": price_data["previous_close"],
        "percent_change": price_data["percent_change"]
    })

df = pd.DataFrame(results)

print("\nFINAL AI TRADING REPORT")
print("=" * 80)
print(df[["ticker", "headline", "sentiment", "confidence", "trading_signal", "current_price", "percent_change"]])

df.to_csv("data/master_report.csv", index=False)

print("\nMaster report saved to data/master_report.csv")