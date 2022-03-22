from bs4 import BeautifulSoup
import requests
import nums_from_string

url = 'http://www.ux.ua/ua/issue.aspx?code=MSICH'
page = requests.get(url)

print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")

table = []

table = soup.findAll("td", class_='pvalue')
tableStr = str(table)
tableFin = tableStr.split(",")
block = tableFin[4]
cenaMassive = nums_from_string.get_nums(block)
cena=''.join(str(x) for x in cenaMassive)

print("Остання угода - ",cena)
print(block)
