
import requests
import json
import os
from os import path


def write_data_to_file(json_data):
	"""
	Stores the conversion data locally in a json file : 
	./files/USD.json. If the parent directory is not exsisting
	it will be created.
	"""
	dir = "./.files/"
	if not path.exists(dir):
		os.mkdir(dir)
	file_name = dir + "USD.json"
	with open(file_name, "w") as jsf:
			f = str(json_data).replace("\'", "\"")
			jsf.write(f)


def write_last_update(json_data):
	"""
	Writes on a file the time of last update of the conversion data
	retreived from the website. If the process went wrong False is
	returned, else it return True.
	"""
	with open("./.files/last_update", "wb") as f:
		try:
			# json_data = requests.get("https://open.er-api.com/v6/latest/USD").json()
			tluu = json_data["time_last_update_unix"]
			encoded_str = str(tluu).encode()#converts a string to a sequence of bytes
			f.write(encoded_str)
			return True
		except Exception:
			return False		
	

def all_currencies():
	"""
	Returns all the currencies from the website (commented) or
	from the local list __all_curr_sorted_list
	"""
	# link = "https://open.er-api.com/v6/latest/USD"
	# try :
	# 	json_data = requests.get(link).json()
	# 	data = json_data["rates"]
	# 	all_currencies = list([i for i in data.keys()])
		# __status = "online"
	# except Exception:
	# 	with open("./.files/USD.json", "r") as jsf:
	# 		json_data = json.load(jsf)
	# 		rates_data = json_data["rates"]
	# 		all_currencies = list([i for i in rates_data.keys()])
	# __status == "offline"
	# else:
	# 	if(is_data_outdataed()):
	# 		write_data_to_file(json_data)
	# 		write_last_update(json_data)
	# return all_currencies
	return __all_curr_sorted_list


def convert(amount, from_currency, to_currency):
	"""
	Converts an amount in a currency to another.
	In case of offline mode, conversion is based on data storded
	locally in a json file from the last online run if data was 
	outdated.
	"""
	from_currency = from_currency.upper()
	to_currency = to_currency.upper()
	link = "https://open.er-api.com/v6/latest/USD"
	file_name = "./.files/USD.json"
	
	try:
		json_data = requests.get(link).json()
		rates_data = json_data["rates"]
	except Exception:
		with open(file_name, "r") as jsf:
			data = json.load(jsf)
			rates_data = data["rates"]
	else:
		if(is_data_outdataed(json_data)):
			write_data_to_file(json_data)
			write_last_update(json_data)

	if(from_currency == "USD"):
		res = amount * rates_data[to_currency]
	elif (to_currency == "USD"):
		res = amount / rates_data[from_currency]
	else:
		res_1 = convert(amount, from_currency, "USD")
		res = convert(res_1, "USD", to_currency)
	return round(res, 4)


def get_status():
	"""
	Returns "online" if the website providind data is reachable
	(internet connection is available), else it returns "offline
	"""
	try:
		requests.get("https://open.er-api.com/v6/latest/USD")
		return "online"
	except Exception:
		return "offline"


def is_data_outdataed(json_data):
	# json_data = requests.get("https://open.er-api.com/v6/latest/USD").json()
	time_last_update_unix = json_data["time_last_update_unix"]
	time_last_update_unix = int(time_last_update_unix)
	last_update = 0
	with open("./.files/last_update", "rb") as f:
		last_update = int(f.read())
	return (time_last_update_unix > last_update)


__all_curr_sorted_list = [
'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS',
'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN',
'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD',
'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF',
'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE',
'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN',
'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL',
'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD',
'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD',
'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW',
'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD',
'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK',
'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN',
'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR',
'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR',
'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF',
'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 
'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL',
'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD',
'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU',
'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD',
'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']

