class NamedEntityRecognizer:

    def __init__(self):
        self.companies = [
            "Apple",
            "Tesla",
            "Microsoft",
            "Amazon",
            "Google",
            "Meta",
            "Nvidia",
            "Netflix",
            "Intel",
            "AMD"
        ]

        self.people = [
            "Elon Musk",
            "Tim Cook",
            "Satya Nadella",
            "Jensen Huang"
        ]

    def extract_entities(self, text):

        entities = {
            "companies": [],
            "people": []
        }

        for company in self.companies:
            if company.lower() in text.lower():
                entities["companies"].append(company)

        for person in self.people:
            if person.lower() in text.lower():
                entities["people"].append(person)

        return entities


if __name__ == "__main__":

    ner = NamedEntityRecognizer()

    headline = "Elon Musk says Tesla will launch a new AI robot"

    entities = ner.extract_entities(headline)

    print("Named Entities Found:")
    print(entities)