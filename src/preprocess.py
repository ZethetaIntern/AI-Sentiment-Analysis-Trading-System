import re
import string


class TextCleaner:
    """
    Cleans financial news headlines and extracts stock tickers.
    """

    def __init__(self):
        self.url_pattern = re.compile(r"http[s]?://\S+")
        self.ticker_pattern = re.compile(r"\$[A-Z]{1,5}")
        self.mention_pattern = re.compile(r"@\w+")

    def remove_urls(self, text):
        return self.url_pattern.sub("", text)

    def remove_mentions(self, text):
        return self.mention_pattern.sub("", text)

    def remove_special_characters(self, text):
        allowed = string.ascii_letters + string.digits + " .,!?$#%"
        return "".join(char for char in text if char in allowed)

    def normalize_whitespace(self, text):
        return " ".join(text.split())

    def extract_tickers(self, text):
        return self.ticker_pattern.findall(text)

    def clean(self, text):
        text = self.remove_urls(text)
        text = self.remove_mentions(text)
        text = self.remove_special_characters(text)
        text = self.normalize_whitespace(text)
        text = text.lower()
        return text


if __name__ == "__main__":
    cleaner = TextCleaner()

    headlines = [
        "BREAKING: $AAPL stock SURGES 5% after earnings beat! https://example.com/news @TradingNews",
        "$TSLA shares fall 3% after weak delivery numbers.",
        "Microsoft announces new AI investment plan."
    ]

    for headline in headlines:
        print("=" * 50)
        print("Original:", headline)
        print("Tickers:", cleaner.extract_tickers(headline))
        print("Cleaned:", cleaner.clean(headline))