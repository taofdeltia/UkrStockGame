from bs4 import BeautifulSoup
import requests
import nums_from_string

code = input("CODE: ")

def name():
	if code == "KVBZ":
		compName="Крюківський вагонобудівний завод"
		print(compName)


class lastPrice:
	url = 'http://www.ux.ua/ua/issue.aspx?code='+code
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")

	table = []
	table = str(soup.findAll("td", class_='pvalue')).split(" ")
	block = table[15].replace(",",".")
	priceArray = nums_from_string.get_nums(block)
	price=''.join(str(x) for x in priceArray)

name()
print("Остання угода - ",lastPrice().price)

