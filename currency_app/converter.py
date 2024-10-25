from datetime import timedelta, datetime
import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('EXCHANGE_API_KEY')
BASE_URL = 'https://api.exchangeratesapi.io/v1/latest'

#To get live exchange rate
def get_exchange_rates():
    params = {'access_key': API_KEY}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        raise Exception("Error fetching exchange rates: " + response.text)

# To convert currency
def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not found.")
    base_amount = amount / rates[from_currency]
    converted_amount = base_amount * rates[to_currency]
    print(f"amount is {amount} convert from {from_currency} to {to_currency}")
    print("converted amount",converted_amount)
    return converted_amount

def get_historical_rates(base_currency, target_currency):
    historical_rates = {}
    for i in range(1, 6):  # Last 5 days
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        historical_url = f'https://api.exchangeratesapi.io/v1/{date}'
        params = {'access_key': API_KEY, 'base': base_currency, 'symbols': target_currency}
        response = requests.get(historical_url, params=params)

        if response.status_code == 200:
            data = response.json()
            historical_rates[date] = data['rates'][target_currency]
        else:
            raise Exception("Error fetching historical rates: " + response.text)

    return historical_rates