class MarketReactionPredictor:

    def __init__(self):
        self.impact_map = {
            "Earnings": {
                "POSITIVE": "Bullish",
                "NEGATIVE": "Bearish",
                "NEUTRAL": "Neutral"
            },
            "Acquisition": {
                "POSITIVE": "Bullish",
                "NEGATIVE": "Uncertain",
                "NEUTRAL": "Neutral"
            },
            "Product Launch": {
                "POSITIVE": "Bullish",
                "NEGATIVE": "Bearish",
                "NEUTRAL": "Neutral"
            },
            "Partnership": {
                "POSITIVE": "Bullish",
                "NEGATIVE": "Uncertain",
                "NEUTRAL": "Neutral"
            },
            "Economic": {
                "POSITIVE": "Bullish",
                "NEGATIVE": "Bearish",
                "NEUTRAL": "Neutral"
            },
            "General News": {
                "POSITIVE": "Mild Bullish",
                "NEGATIVE": "Mild Bearish",
                "NEUTRAL": "Neutral"
            }
        }

    def predict_reaction(self, event_type, sentiment, confidence):
        sentiment = sentiment.upper()

        reaction = self.impact_map.get(
            event_type,
            self.impact_map["General News"]
        ).get(sentiment, "Neutral")

        if confidence >= 0.85:
            reaction_confidence = "High"
        elif confidence >= 0.65:
            reaction_confidence = "Medium"
        else:
            reaction_confidence = "Low"

        expected_move = self.estimate_price_move(reaction, confidence)

        return {
            "market_reaction": reaction,
            "reaction_confidence": reaction_confidence,
            "expected_price_move": expected_move
        }

    def estimate_price_move(self, reaction, confidence):
        if reaction == "Bullish":
            return f"+{round(confidence * 3, 2)}%"
        elif reaction == "Mild Bullish":
            return f"+{round(confidence * 1.5, 2)}%"
        elif reaction == "Bearish":
            return f"-{round(confidence * 3, 2)}%"
        elif reaction == "Mild Bearish":
            return f"-{round(confidence * 1.5, 2)}%"
        elif reaction == "Uncertain":
            return "0% to ±1%"
        else:
            return "0%"


if __name__ == "__main__":

    predictor = MarketReactionPredictor()

    test_cases = [
        ("Earnings", "POSITIVE", 0.92),
        ("Earnings", "NEGATIVE", 0.88),
        ("Product Launch", "POSITIVE", 0.76),
        ("Economic", "NEGATIVE", 0.81),
        ("General News", "NEUTRAL", 0.70)
    ]

    for event_type, sentiment, confidence in test_cases:
        result = predictor.predict_reaction(event_type, sentiment, confidence)

        print("-----------------------------")
        print("Event Type :", event_type)
        print("Sentiment  :", sentiment)
        print("Confidence :", confidence)
        print("Reaction   :", result["market_reaction"])
        print("Strength   :", result["reaction_confidence"])
        print("Expected Move:", result["expected_price_move"])