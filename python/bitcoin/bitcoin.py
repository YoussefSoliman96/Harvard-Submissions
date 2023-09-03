import requests
import sys

if len(sys.argv) < 2:
    sys.exit(print("Too few arguments"))
if len(sys.argv) > 2:
    sys.exit(print("Too many arguments"))
else:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_price = r.json()["bpi"]["USD"]["rate_float"]
    try:
        print(r.json()["bpi"]["USD"]["rate_float"])
    except requests.RequestException:
        sys.exit(1)