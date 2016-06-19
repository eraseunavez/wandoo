import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	page = 1
	while page < max_pages:
		url = 'http://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'lxml')
		print soup.select('table')
		page += 1

spider(25)