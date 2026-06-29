import pandas as pd

# Read the sentiment results
df = pd.read_csv("data/sentiment_results.csv")


def generate_signal(sentiment):
    if sentiment == "POSITIVE":
        return "BUY"

    elif sentiment == "NEGATIVE":
        return "SELL"

    else:
        return "HOLD"


# Create a new column
df["Trading Signal"] = df["Sentiment"].apply(generate_signal)

print(df)

# Save the updated results
df.to_csv("data/trading_signals.csv", index=False)

print("\nTrading signals generated successfully!")