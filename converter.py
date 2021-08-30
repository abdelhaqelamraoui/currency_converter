
import requests
import json
import os
from os import path
from sys import stderr

def convert(amount, from_currency, to_currency):
	from_currency = from_currency.upper()
	to_currency = to_currency.upper()

	dir = "./.json_files/"
	if not path.exists(dir):
		os.mkdir(dir)

	link = "https://open.er-api.com/v6/latest/" + from_currency
	file_name = dir + from_currency+".json"

	try:
		json_data = requests.get(link).json()
		rates_data = json_data["rates"]
		all_currencies = list([ i for i in rates_data.keys()])
		# print(all_currencies)

		with open(file_name, "w") as jsf:
			f = str(json_data).replace("\'", "\"")
			jsf.write(f)

	except Exception:
		print("-------OFFLINE MODE-------")
		with open(file_name, "r") as jsf:
			data = json.load(jsf)
			rates_data = data["rates"]	
	# else:
		# for i in all_currencies:
		# 	link = "https://open.er-api.com/v6/latest/" + i
		# 	file_name = dir + i +".json"
		# 	with open(file_name, "w") as jsf:
		# 		json_data = requests.get(link).json()
		# 		f = str(json_data).replace("\'", "\"")
		# 		jsf.write(f)

	return round(amount * rates_data[to_currency], 4)
	
# amount = int(input("Amount : "))
# from_currency = input("From   : ")
# to_currency = input("To     : ")

# res = convert(amount, from_currency, to_currency)
# print("{} {} = {} {}".format(amount, from_currency, res, to_currency))

