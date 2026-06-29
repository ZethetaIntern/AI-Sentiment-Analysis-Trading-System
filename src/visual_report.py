import os
import pandas as pd
import matplotlib.pyplot as plt

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/master_report.csv")

# Trading Signals
plt.figure(figsize=(6,4))
df["trading_signal"].value_counts().plot(kind="bar")
plt.title("Trading Signal Distribution")
plt.tight_layout()
plt.savefig("outputs/trading_signal_distribution.png")
plt.close()

# Sentiments
plt.figure(figsize=(6,4))
df["sentiment"].value_counts().plot(kind="bar")
plt.title("Sentiment Distribution")
plt.tight_layout()
plt.savefig("outputs/sentiment_distribution.png")
plt.close()

# Confidence
plt.figure(figsize=(8,4))
df["confidence"].plot(kind="bar")
plt.title("Confidence Scores")
plt.tight_layout()
plt.savefig("outputs/confidence_scores.png")
plt.close()

print("Charts created successfully!")