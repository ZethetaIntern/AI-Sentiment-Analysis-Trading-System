class EventClassifier:

    def __init__(self):

        self.events = {
            "Earnings": [
                "earnings",
                "profit",
                "revenue",
                "quarter",
                "results"
            ],

            "Acquisition": [
                "acquire",
                "acquisition",
                "buyout",
                "merge",
                "merger"
            ],

            "Product Launch": [
                "launch",
                "introduces",
                "unveils",
                "release"
            ],

            "Partnership": [
                "partnership",
                "collaboration",
                "agreement",
                "deal"
            ],

            "Economic": [
                "inflation",
                "interest rate",
                "fed",
                "gdp",
                "economy"
            ]
        }

    def classify(self, headline):

        headline = headline.lower()

        for event, keywords in self.events.items():

            for keyword in keywords:

                if keyword in headline:
                    return event

        return "General News"


if __name__ == "__main__":

    classifier = EventClassifier()

    headlines = [

        "Apple beats earnings expectations",

        "Microsoft acquires AI startup",

        "Tesla launches new robot",

        "Federal Reserve raises interest rates",

        "Nvidia signs partnership with OpenAI"

    ]

    for headline in headlines:

        event = classifier.classify(headline)

        print("-----------------------------")
        print("Headline :", headline)
        print("Event    :", event)