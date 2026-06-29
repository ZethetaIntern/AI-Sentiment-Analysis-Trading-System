import requests
from news_api import API_KEY


def get_stock_price(ticker):
    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": ticker,
        "token": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching stock price:", response.status_code)
        return None

    data = response.json()

    return {
        "ticker": ticker,
        "current_price": data.get("c"),
        "previous_close": data.get("pc"),
        "change": data.get("d"),
        "percent_change": data.get("dp")
    }


if __name__ == "__main__":
    ticker = input("Enter stock ticker: ").upper()

    price_data = get_stock_price(ticker)

    print("\nSTOCK PRICE DATA")
    print("=" * 50)
    print("Ticker:", price_data["ticker"])
    print("Current Price:", price_data["current_price"])
    print("Previous Close:", price_data["previous_close"])
    print("Change:", price_data["change"])
    print("Percent Change:", price_data["percent_change"])