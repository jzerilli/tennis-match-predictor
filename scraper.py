from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.options import Options
import bs4
import requests

# https://www.ultimatetennisstatistics.com/headToHead?name1=Rafael%20Nadal&name2=Novak%20Djokovic
# https://www.ultimatetennisstatistics.com/playerProfile?playerId=3819&tab=statistics&surface=G&season=-1

# https://www.ultimatetennisstatistics.com/playerProfile?playerId=3819&tab=matches&season=&fromDate=&toDate=&level=&bestOf=&surface=G&indoor=&speed=&round=&result=&tournamentId=&opponent=&countryId=&outcome=played

# def getPlayerPage(driver, player_name):
# 	search=driver.find_element_by_id('player')
# 	search.send_keys(player_name)

# 	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-1"]/li[1]'))).click()

def getPlayerStats(driver, player_name, surface):
	url = f'https://www.ultimatetennisstatistics.com/playerProfile?name={player_name}'
	driver.get(url)

	html = driver.find_element_by_xpath('//*[@id="profile"]/div').get_attribute('innerHTML')
	soup = bs4.BeautifulSoup(html, features="lxml")

	tables = soup.findAll("table")
	bio_table = tables[0]  
	rank_table = tables[1] 

	age = bio_table.find("th", text="Age").find_next_sibling("td").text
	age = int(age[:age.find(' ')])
	height = bio_table.find("th", text="Height").find_next_sibling("td").text
	height = int(height[:height.find(' ')])
	hand = bio_table.find("th", text="Plays").find_next_sibling("td").text
	if hand == 'Left-handed':
		hand = 1
	else:
		hand = 0

	rank = rank_table.find("th", text="Current Rank").find_next_sibling("td").text
	rank = int(rank[:rank.find(' ')])
	
	url = f'https://www.ultimatetennisstatistics.com/playerProfile?name={player_name}&tab=statistics&season=-1'
	driver.get(url)
	html = driver.find_element_by_xpath('//*[@id="playerStatsTab"]').get_attribute('innerHTML')
	soup = bs4.BeautifulSoup(html, features="lxml")

	tables = soup.findAll("table")

	serve_table = tables[0]  
	return_table = tables[1] 
	total_table = tables[2] 

	ace_pct = float(serve_table.find("td", text="Ace %").find_next_sibling("th").text[:-1])/100
	fst_serve_pct = float(serve_table.find("td", text="1st Serve %").find_next_sibling("th").text[:-1])/100
	serve_pt_pct = float(serve_table.find("td", text="Service Points Won %").find_next_sibling("th").text[:-1])/100
	bp_save_pct = float(serve_table.find("td", text="Break Points Saved %").find_next_sibling("th").text[:-1])/100

	break_pct = float(return_table.find("td", text="Break Points Won %").find_next_sibling("th").text[:-1])/100
	return_pt_pct = float(return_table.find("td", text="Return Points Won %").find_next_sibling("th").text[:-1])/100

	win_pct = float(total_table.find("td", text="Matches Won %").find_next_sibling("th").text.strip('\n')[:-1])/100

	url = f'https://www.ultimatetennisstatistics.com/playerProfile?name={player_name}&tab=statistics&season=-1&surface={surface}'
	driver.get(url)

	html = driver.find_element_by_xpath('//*[@id="playerStatsTab"]').get_attribute('innerHTML')
	soup = bs4.BeautifulSoup(html, features="lxml")

	tables = soup.findAll("table")
	total_table = tables[2] 

	# surface_ace_pct = float(serve_table.find("td", text="Ace %").find_next_sibling("th").text[:-1])/100
	# surface_fst_serve_pct = float(serve_table.find("td", text="1st Serve %").find_next_sibling("th").text[:-1])/100
	# surface_serve_pt_pct = float(serve_table.find("td", text="Service Points Won %").find_next_sibling("th").text[:-1])/100
	# surface_bp_save_pct = float(serve_table.find("td", text="Break Points Saved %").find_next_sibling("th").text[:-1])/100

	# surface_break_pct = float(return_table.find("td", text="Break Points Won %").find_next_sibling("th").text[:-1])/100
	# surface_return_pt_pct = float(return_table.find("td", text="Return Points Won %").find_next_sibling("th").text[:-1])/100

	surface_win_pct = float(total_table.find("td", text="Matches Won %").find_next_sibling("th").text.strip('\n')[:-1])/100


	return (rank, age, height, hand, fst_serve_pct, ace_pct, bp_save_pct, serve_pt_pct, break_pct, return_pt_pct, win_pct, surface_win_pct)


def getHeadToHead(driver, p1, p2):
	url = f'https://www.ultimatetennisstatistics.com/headToHead?name1={p1}&name2={p2}'
	driver.get(url)
	html = driver.page_source
	soup = bs4.BeautifulSoup(html, features="lxml")

	table = soup.find("table")
	p1_wins = int(table.find("th", text="H2H").find_previous_sibling("th").text)
	p2_wins = int(table.find("th", text="H2H").find_next_sibling("th").text)
	return (p1_wins, p2_wins)


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome('./chromedriver', options = chrome_options)

# t0 = time.time()
# print(getPlayerStats(driver, 'Roger Federer', 'C'))
# print(getPlayerStats(driver, 'Novak Djokovic', 'C'))
# print(getHeadToHead(driver, 'Roger Federer', 'Novak Djokovic'))

# t1 = time.time()
# print(t1-t0)
# driver.quit()


