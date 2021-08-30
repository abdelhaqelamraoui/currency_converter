
import requests
import json
import os
from os import path
from sys import stderr


def write_data_to_file(json_data):
	dir = "./.json_files/"
	if not path.exists(dir):
		os.mkdir(dir)
	file_name = dir + "USD.json"
	with open(file_name, "w") as jsf:
			f = str(json_data).replace("\'", "\"")
			jsf.write(f)

def all_currencies():
	link = "https://open.er-api.com/v6/latest/USD"
	try :
		json_data = requests.get(link).json()
		data = json_data["rates"]
		all_currencies = list([i for i in data.keys()])
	except Exception:
		with open("./.json_files/USD.json", "r") as jsf:
			json_data = json.load(jsf)
			rates_data = json_data["rates"]
			all_currencies = list([i for i in rates_data.keys()])
	else:
		write_data_to_file(json_data)

	return all_currencies



def convert(amount, from_currency, to_currency):
	from_currency = from_currency.upper()
	to_currency = to_currency.upper()
	link = "https://open.er-api.com/v6/latest/USD"
	file_name = "./.json_files/USD.json"
	
	try:
		json_data = requests.get(link).json()
		rates_data = json_data["rates"]
	except Exception:
		with open(file_name, "r") as jsf:
			data = json.load(jsf)
			rates_data = data["rates"]	
	else:
		write_data_to_file(json_data)

	if(from_currency == "USD"):
		res = amount * rates_data[to_currency]
	elif (to_currency == "USD"):
		res = amount / rates_data[from_currency]
	else:
		res_1 = convert(amount, from_currency, "USD")
		res = convert(res_1, "USD", to_currency)
	return round(res, 4)
	

# amount = int(input("Amount : "))
# from_currency = input("From   : ")
# to_currency = input("To     : ")

# result = convert(amount, from_currency, to_currency)
# print("{} {} = {} {}".format(amount, from_currency.upper(), result, to_currency.upper()))




	# else:
		# for i in all_currencies:
		# 	link = "https://open.er-api.com/v6/latest/" + i
		# 	file_name = dir + i +".json"
		# 	with open(file_name, "w") as jsf:
		# 		json_data = requests.get(link).json()
		# 		f = str(json_data).replace("\'", "\"")
		# 		jsf.write(f)