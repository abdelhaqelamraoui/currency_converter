
import requests
import json
from sys import stderr

def dollor_converter(amount, from_currency, to_currency):
	from_currency = from_currency.upper()
	to_currency = to_currency.upper()

	link = "https://open.er-api.com/v6/latest/USD"
	file_name = from_currency+".json"

	try:
		json_data = requests.get(link).json()
		rates_data = json_data["rates"]

		with open(file_name, "w") as jsf:
			f = str(json_data).replace("\'", "\"")
			jsf.write(f)

	except Exception:
		print("----OFFLINE MODE----")
		with open(file_name, "r") as jsf:
			data = json.load(jsf)
			rates_data = data["rates"]	

	if(from_currency != "USD"):
		res = amount / rates_data[from_currency]
	else:
		res = amount * rates_data[to_currency]
	return round(res, 4)
	
amount = int(input("Amount : "))
from_currency = input("From   : ")
to_currency = input("To     : ")

res = dollor_converter(amount, from_currency, to_currency)
print("{} {} = {} {}".format(amount, from_currency, res, to_currency))

