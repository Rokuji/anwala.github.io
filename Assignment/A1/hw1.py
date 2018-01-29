import requests
import sys
from bs4 import BeautifulSoup

# main
website= sys.argv[1]
url = website
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
	try:
		if link['href'].startswith('https:') or link['href'].startswith('http:') :
			if link['href'].endswith('.pdf'):
				res = requests.head(link['href'])
				res.headers 
				{'content-length': ''}
				print (link.get('href'), res.headers['content-length'], "Bytes")
			else:
				print(link.get('href'))
	except KeyError:
		pass
	