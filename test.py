import json
import ast
  
# # Opening JSON file
# f = open('USD.json',)
  
# # returns JSON object as 
# # a dictionary
# data = json.load(json.dumps(f))


# # mixing single and double quotes
# data = {'jsonKey': 'jsonValue',"title": "hello world"}

# # get string with all double quotes
# json_string = json.dumps(data) 

# print(json_string)
#   

with open('USD.json', "r") as jsf:
	f = jsf.read()
	f = f.replace('\'', "\"")
	data =json.dumps(jsf)
	print(dic)
	# rates_data = data["rates"]



# import json

# # mixing single and double quotes
# data = {'jsonKey': 'jsonValue',"title": "hello world"}

# # get string with all double quotes
# json_string = json.dumps(data) 
# print(json_string)


