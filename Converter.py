
import requests
from sys import stderr

def dollor_converter(amount, from_currency, to_currency):
	try:
		link = "https://open.er-api.com/v6/latest/USD"
		json_data = requests.get(link).json()
		rates_data = json_data["rates"]
	except Exception:
		print("No internet connection !", file=stderr)
		return None
	else:
		if(from_currency.upper() != "USD"):
			res = amount / rates_data[from_currency.upper()]
		res = amount * rates_data[to_currency.upper()]
		return round(res, 4)
	

amount = int(input("Amount : "))
from_currency = input("From   : ")
to_currency = input("To     : ")

res = dollor_converter(amount, from_currency, to_currency)

print("{} {} = {} {}".format(amount, from_currency, res, to_currency))

