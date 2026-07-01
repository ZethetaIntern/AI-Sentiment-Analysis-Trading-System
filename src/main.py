from news_api import fetch_company_news
from stock_price import get_stock_price
from preprocess import TextCleaner
from finbert_sentiment import FinBERTSentimentAnalyzer
from ner import NamedEntityRecognizer
from event_classifier import EventClassifier
from market_reaction import MarketReactionPredictor
import pandas as pd


def generate_signal(sentiment, market_reaction):
    if sentiment == "POSITIVE" and "Bullish" in market_reaction:
        return "BUY"
    elif sentiment == "NEGATIVE" and "Bearish" in market_reaction:
        return "SELL"
    else:
        return "HOLD"


ticker = input("Enter stock ticker: ").upper()

print("\nDownloading real financial news...")
news = fetch_company_news(ticker)

print("Getting stock price...")
price_data = get_stock_price(ticker)

cleaner = TextCleaner()
sentiment_analyzer = FinBERTSentimentAnalyzer()
ner = NamedEntityRecognizer()
event_classifier = EventClassifier()
reaction_predictor = MarketReactionPredictor()

results = []

for item in news[:10]:
    headline = item.get("headline", "")
    cleaned = cleaner.clean(str(headline))

    entities = ner.extract_entities(headline)
    event_type = event_classifier.classify(headline)

    sentiment_result = sentiment_analyzer.analyze(cleaned)
    sentiment = sentiment_result["sentiment"]
    confidence = sentiment_result["confidence"]

    reaction_result = reaction_predictor.predict_reaction(
        event_type,
        sentiment,
        confidence
    )

    market_reaction = reaction_result["market_reaction"]
    reaction_confidence = reaction_result["reaction_confidence"]
    expected_price_move = reaction_result["expected_price_move"]

    signal = generate_signal(sentiment, market_reaction)

    results.append({
        "ticker": ticker,
        "headline": headline,
        "cleaned_headline": cleaned,
        "companies": ", ".join(entities["companies"]),
        "people": ", ".join(entities["people"]),
        "event_type": event_type,
        "sentiment": sentiment,
        "confidence": confidence,
        "market_reaction": market_reaction,
        "reaction_confidence": reaction_confidence,
        "expected_price_move": expected_price_move,
        "trading_signal": signal,
        "current_price": price_data["current_price"],
        "previous_close": price_data["previous_close"],
        "percent_change": price_data["percent_change"]
    })

df = pd.DataFrame(results)

print("\nFINAL ENHANCED AI TRADING REPORT")
print("=" * 100)
print(df[[
    "ticker",
    "headline",
    "companies",
    "event_type",
    "sentiment",
    "market_reaction",
    "expected_price_move",
    "trading_signal"
]])

df.to_csv("data/master_report.csv", index=False)

print("\nEnhanced master report saved to data/master_report.csv")