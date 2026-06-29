from preprocess import TextCleaner
from sentiment import SimpleSentimentAnalyzer
import pandas as pd

cleaner = TextCleaner()
analyzer = SimpleSentimentAnalyzer()

headlines = [
    "Apple beats earnings expectations by 20%",
    "Tesla reports weak quarterly deliveries",
    "Microsoft announces new AI investment",
    "Amazon posts record profit growth",
    "Meta faces lawsuit over user privacy"
]

results = []

for headline in headlines:

    cleaned = cleaner.clean(headline)

    sentiment = analyzer.analyze(cleaned)

    results.append({
        "Original": headline,
        "Cleaned": cleaned,
        "Sentiment": sentiment
    })

df = pd.DataFrame(results)

print(df)

df.to_csv("data/sentiment_results.csv", index=False)

print("\nPipeline completed successfully!")