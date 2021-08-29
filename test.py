
import requests

def convertor(from_currency,to_currency,money):
	link="https://open.er-api.com/v6/latest/USD"
	req=requests.get(link).json()
	rates_data=req['rates']
	# if from_currency != 'USD' :
	# 	from_currency = input("enter usd currency : ")
	money=round(money *rates_data[to_currency], 4)
	return money

print("100$ = ", convertor('USD',"MAD",100))