import requests
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit(1)
if len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit(1)
else:

    # Convert the user input to float
    bitcoin_amount = float(sys.argv[1])
    # Get the API response
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Get the bitcoin price
    bitcoin_price = r.json()["bpi"]["USD"]["rate_float"]
    # Get the total price of the bitcoins the user requested
    total_price = bitcoin_amount * bitcoin_price
    print(f"${total_price:,.4f}")
