import pandas as pd

news = [
    {
        "ticker": "AAPL",
        "headline": "Apple beats earnings expectations",
        "sentiment": "Positive"
    },
    {
        "ticker": "TSLA",
        "headline": "Tesla shares fall after weak deliveries",
        "sentiment": "Negative"
    },
    {
        "ticker": "MSFT",
        "headline": "Microsoft announces new AI investment",
        "sentiment": "Neutral"
    }
]

df = pd.DataFrame(news)

print(df)

df.to_csv("data/news.csv", index=False)

print("\nNews saved successfully!")