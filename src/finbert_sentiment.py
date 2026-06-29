from transformers import pipeline


class FinBERTSentimentAnalyzer:

    def __init__(self):
        self.model = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert"
        )

    def analyze(self, text):
        result = self.model(text)[0]

        return {
            "sentiment": result["label"].upper(),
            "confidence": round(result["score"], 4)
        }


if __name__ == "__main__":
    analyzer = FinBERTSentimentAnalyzer()

    headlines = [
        "Apple beats earnings expectations as iPhone sales rise",
        "Tesla shares fall after weak delivery numbers",
        "Microsoft announces new AI investment plan"
    ]

    for headline in headlines:
        result = analyzer.analyze(headline)

        print("=" * 70)
        print("Headline:", headline)
        print("Sentiment:", result["sentiment"])
        print("Confidence:", result["confidence"])