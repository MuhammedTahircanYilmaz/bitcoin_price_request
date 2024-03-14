import sys
import requests
import json

def main():
    if len(sys.argv) < 2 :
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("There are too many command-line arguments")
        sys.exit(1)

    try:
        bitcoin_num = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = response.json()
    rate = bitcoin["bpi"]["USD"]["rate"]
    rate_cleaned = float(rate.replace(",",""))
    amount = rate_cleaned * bitcoin_num
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main() 