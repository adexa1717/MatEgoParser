import openpyxl
import requests
from bs4 import BeautifulSoup as BS

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'
}
base_url = 'https://grouple.co/news/elements?offset=0&max=50'

wb = openpyxl.load_workbook('elem.xlsx')
sheet_ranges = wb['Sheet1']
sheet_ranges['A1'].value = 'Список манги, обновления:'
index = 1
request = requests.get(base_url, headers=headers)

html = BS(request.content, 'lxml')

print(html)
for title in html.select('.site-element'):
    sheet_ranges['A' + str(index + 1)].value = title[0].text
    index += 1

wb.save('elem.xlsx')
