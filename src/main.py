import json
import os

import requests

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

print(API_KEY)


def get_currency(currency: str) -> float:
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"

    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    return rate


def save_to_json():
    pass
