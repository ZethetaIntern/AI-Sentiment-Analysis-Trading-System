from preprocess import TextCleaner
from finbert_sentiment import FinBERTSentimentAnalyzer
import pandas as pd


cleaner = TextCleaner()
analyzer = FinBERTSentimentAnalyzer()


def generate_signal(sentiment):
    if sentiment == "POSITIVE":
        return "BUY"
    elif sentiment == "NEGATIVE":
        return "SELL"
    else:
        return "HOLD"


df = pd.read_csv("data/real_news.csv")

cleaned_headlines = []
sentiments = []
confidences = []
signals = []

for headline in df["headline"]:
    cleaned = cleaner.clean(str(headline))

    result = analyzer.analyze(cleaned)

    sentiment = result["sentiment"]
    confidence = result["confidence"]

    signal = generate_signal(sentiment)

    cleaned_headlines.append(cleaned)
    sentiments.append(sentiment)
    confidences.append(confidence)
    signals.append(signal)

df["cleaned_headline"] = cleaned_headlines
df["sentiment"] = sentiments
df["confidence"] = confidences
df["trading_signal"] = signals

print(df[["ticker", "headline", "sentiment", "confidence", "trading_signal"]])

df.to_csv("data/final_report.csv", index=False)

print("\nFinal report saved to data/final_report.csv")