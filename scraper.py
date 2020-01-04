from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


def getPlayerPage(driver, player_name):
	driver.get("https://www.ultimatetennisstatistics.com/")
	search=driver.find_element_by_id('player')
	search.send_keys(player_name)
	time.sleep(1)
	search=driver.find_element_by_id('ui-id-1')

	items = search.find_elements_by_tag_name("li")
	items[0].click()

def getPlayerStats(driver, player_name, surface):
	getPlayerPage(driver, player_name)
	#select statistcs tab
	statstab=driver.find_element_by_xpath('//*[@id="playerPills"]/li[9]/a').click()
	statstab=driver.find_element_by_xpath('//*[@id="statisticsPill"]').click()
	time.sleep(1)

	#set date filter to past year
	date_range = Select(driver.find_element_by_xpath('//*[@id="statsSeason"]'))
	date_range.select_by_value('-1')
	time.sleep(1)


	serve_table = driver.find_element_by_xpath('//*[@id="statisticsOverview"]/div/div[1]/table')
	serve_rows = serve_table.find_elements(By.TAG_NAME, "tr")

	return_table=driver.find_element_by_xpath('//*[@id="statisticsOverview"]/div/div[2]/table')
	return_rows = return_table.find_elements(By.TAG_NAME, "tr")

	stats = serve_rows[1].text, serve_rows[3].text, serve_rows[6].text, return_rows[5].text, return_rows[6].text

	#repeat for surface specific data
	surface_filter = Select(driver.find_element_by_xpath('//*[@id="statsSurface"]'))
	surface_filter.select_by_value(surface)
	time.sleep(1)

	surface_serve_table = driver.find_element_by_xpath('//*[@id="statisticsOverview"]/div/div[1]/table')
	surface_serve_rows = surface_serve_table.find_elements(By.TAG_NAME, "tr")

	surface_return_table=driver.find_element_by_xpath('//*[@id="statisticsOverview"]/div/div[2]/table')
	surface_return_rows = surface_return_table.find_elements(By.TAG_NAME, "tr")

	surface_stats = surface_serve_rows[1].text, surface_serve_rows[3].text, surface_serve_rows[6].text, surface_return_rows[5].text, surface_return_rows[6].text

	get_raw = lambda a: float(a[a.find('%') + 1: -1])/100
	return tuple(map(get_raw, stats)), tuple(map(get_raw, surface_stats))

def getHeadToHead(driver, p1, p2):
	getPlayerPage(driver, p1)
	search=driver.find_element_by_id('h2hPlayer')
	search.send_keys(p2)
	time.sleep(1)
	search=driver.find_element_by_id('ui-id-2')
	items = search.find_elements_by_tag_name("li")
	items[0].click()
	time.sleep(1)

	p1_wins = int(driver.find_element_by_xpath('//*[@id="profiles"]/table/tbody/tr[2]/th[1]').text)
	p2_wins = int(driver.find_element_by_xpath('//*[@id="profiles"]/table/tbody/tr[2]/th[3]').text)

	return p1_wins, p2_wins


	



driver=webdriver.Chrome('./chromedriver')
time.sleep(1)
x = getPlayerStats(driver, 'Roger Federer','C')
print('fed stats ', x)
x = getPlayerStats(driver,'Novak Djokovic', 'C')
print('djoko stats ', x)
h2h = getHeadToHead(driver, 'Roger Federer', 'Novak Djokovic')
print('h2h ', h2h)

# driver.close()


