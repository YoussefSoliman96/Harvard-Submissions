import requests
import sys

if len(sys.argv) < 2:
    sys.exit(print("Too few arguments"))
if len(sys.argv) > 2:
    sys.exit(print("Too many arguments"))
else:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        print(r.json())
    except requests.RequestException:
        sys.exit(1)