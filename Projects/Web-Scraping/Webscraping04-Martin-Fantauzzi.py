import requests
import bs4
res = requests.get('https://www.sanignacio.pr')
res.raise_for_status()
SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
elems = SanIgnaciopr.select('#paragraph')
print(type(SanIgnaciopr))
print(len(elems))


