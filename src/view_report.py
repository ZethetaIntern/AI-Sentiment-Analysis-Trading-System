import pandas as pd

df = pd.read_csv("data/final_report.csv")

print("\nFINAL NEWS SENTIMENT REPORT")
print("=" * 90)

for index, row in df.iterrows():
    print("Ticker:", row["ticker"])
    print("Headline:", row["headline"])
    print("Sentiment:", row["sentiment"])
    print("Confidence:", row["confidence"])
    print("Signal:", row["trading_signal"])
    print("-" * 90)