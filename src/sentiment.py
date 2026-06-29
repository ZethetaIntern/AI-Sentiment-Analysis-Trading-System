from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SimpleSentimentAnalyzer:

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):

        scores = self.analyzer.polarity_scores(text)

        compound = scores["compound"]

        if compound >= 0.05:
            return "POSITIVE"

        elif compound <= -0.05:
            return "NEGATIVE"

        else:
            return "NEUTRAL"