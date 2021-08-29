

import requests

def convertor(from_currency,to_currency,amount):
	link="https://open.er-api.com/v6/latest/USD"
	req=requests.get(link).json()
	rates_data=req['rates']
	if from_currency != 'USD':
		amount = amount / rates_data[from_currency] 
        
	amount=round(amount *rates_data[to_currency], 4)
	return amount

amount=int(input('enter amount : '))
to_currency=input('enter currency : ')
from_currency=input('enter currency : ')
print(str(amount),str(from_currency), convertor(from_currency,to_currency,amount),str(to_currency))