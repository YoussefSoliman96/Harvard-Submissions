import requests
import sys

if len(sys.argv) < 2:
    sys.exit(print("Too few arguments"))
else:
    r = requests.get(https://api.coindesk.com/v1/bpi/currentprice.json)
    print(r)
