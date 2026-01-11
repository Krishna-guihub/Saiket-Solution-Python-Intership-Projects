import requests

api_url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    rates = data["rates"]

    print("Welcome to the Currency Converter!")
    print("Supported currencies:", ", ".join(list(rates.keys())[:10]), "etc.\n")

    from_currency = input("Convert from (e.g., USD): ").upper()
    to_currency = input("Convert to (e.g., EUR): ").upper()
    amount = input("Enter amount: ")

    if from_currency not in rates or to_currency not in rates:
        print("Error: Unsupported currency code.")
    else:
        try:
            amount = float(amount)
            usd_amount = amount / rates[from_currency]  # convert to USD
            converted = usd_amount * rates[to_currency]
            print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
        except ValueError:
            print("Error: Please enter a valid number.")

except requests.exceptions.RequestException as e:
    print("Error fetching exchange rates:", e)
