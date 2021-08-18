import requests

def limpiar_str(string):
	caracteres = '<>/$#@%&!*'
	for i in caracteres:
		string = string.replace(i,'')
	return string

def generar_cat():
	params = {'limit':10}
	response = requests.get("https://api.thecatapi.com/v1/images/search",params=params)
	response_json = response.json()

	gatos = []

	for i in response_json:
		gatos.append(i["url"])

	return gatos

if __name__ == '__main__':
	print(generar_cat())