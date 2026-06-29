import requests
import pandas as pd
from datetime import datetime, timedelta


API_KEY = "d90nechr01qj6uru9ltgd90nechr01qj6uru9lu0"


def fetch_company_news(ticker):
    today = datetime.today()
    seven_days_ago = today - timedelta(days=7)

    url = "https://finnhub.io/api/v1/company-news"

    params = {
        "symbol": ticker,
        "from": seven_days_ago.strftime("%Y-%m-%d"),
        "to": today.strftime("%Y-%m-%d"),
        "token": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return []

    data = response.json()
    return data


if __name__ == "__main__":
    ticker = input("Enter Stock Ticker (Example: AAPL, TSLA, MSFT): ").upper()
    news = fetch_company_news(ticker)

    results = []

    for item in news[:10]:
        results.append({
            "ticker": ticker,
            "headline": item.get("headline"),
            "summary": item.get("summary"),
            "source": item.get("source"),
            "datetime": item.get("datetime"),
            "url": item.get("url")
        })

    df = pd.DataFrame(results)

    print(df)

    df.to_csv("data/real_news.csv", index=False)

    print("\nReal financial news saved to data/real_news.csv")