import openpyxl
import requests
from bs4 import BeautifulSoup as BS 
headers = {
	'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'
}
base_url = 'https://readmanga.me/list?sortType=created&offset='

pages = []
wb = openpyxl.load_workbook('demo.xlsx')
sheet_ranges = wb['Sheet1']
sheet_ranges['A1'].value = 'Список манги, новинки:'
index = 1
session = requests.Session()
request = session.get(base_url, headers = headers)
html = BS(request.content, 'html.parser')

try:
	padination =  html.select('a.step')
except:
	pass

for x in range(0,int(padination[-1].text)):
	pages.append(requests.get(f'https://readmanga.me/list?sortType=created&offset={str(x*70)}'))

for r in pages:
	html = BS(r.content, 'lxml')
	try:
		padination =  html.select('a.step')
	except:
		pass

	for e in html.select('.col-sm-6'):
		title = e.select('.desc > h3')
		sheet_ranges['A'+str(index+1)].value = title[0].text
		index+=1



wb.save('demo.xlsx')














































