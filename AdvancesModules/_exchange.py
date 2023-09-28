import requests 
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

def convert_currency():
    base_currency = input("Base Currency: ")
    target_currency = input("Target Currency: ")

    amount = float(input(f"How much {base_currency} do you want to convert?: "))

    response = requests.get(api_url + base_currency)
    data = json.loads(response.text)

    exchange_rate = data['rates'][target_currency]

    converted_amount = amount * exchange_rate

    print(f"1 {base_currency} = {exchange_rate} {target_currency}")
    print(f"{amount} {base_currency} = {converted_amount} {target_currency}")

if __name__ == "__main__":
    convert_currency()
