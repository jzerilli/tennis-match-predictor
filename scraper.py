from bs4 import BeautifulSoup
import requests

page_link = 'https://www.atptour.com/en/players/stefanos-tsitsipas/te51/player-stats?year=2017&surfaceType=all'

page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library
soup = BeautifulSoup(page_response.content, "html.parser")

tables = soup.findAll('table', {'class': 'mega-table'})

for table in tables:
	rows = table.find("tbody").find_all("tr")
	for row in rows:
		print(row)


