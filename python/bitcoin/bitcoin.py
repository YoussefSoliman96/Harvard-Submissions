import requests
import sys

if len(sys.argv) < 2:
    sys.exit(print("Too few arguments"))
if len(sys.argv) > 2:
    sys.exit(print("Too many arguments"))
else:
    # Get the API response
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Convert the user input to float
    bitcoin_amount = float(sys.argv[1])
    # Get the bitcoin price
    bitcoin_price = r.json()["bpi"]["USD"]["rate_float"]
    # Get the total price of the bitcoins the user requested
    total_price = bitcoin_amount * bitcoin_price
    try:
        print(f"${total_price:.4f}")
    except requests.RequestException:
        sys.exit(1)