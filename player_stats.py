from selenium import webdriver
import selenium
import collections
import time
import csv

driver = webdriver.Chrome()

driver.get('http://stats.nba.com/players/traditional/?sort=PTS&dir=-1')
driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()
time.sleep(25)

csv_file = open('nbaplayerstats.csv', 'w')
writer = csv.writer(csv_file)
header=['PLAYER', 'TEAM', 'AGE', 'GP', 'W', 'L', 'MIN', 'PTS', 'FG%', '3P%','FTM', 'FTA', 'FT%', 'FP', 'DD2', 'TD3', '+/-', 'FGM', 'FGA', '3PM', '3PA', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'PF']
writer.writerow(header)

players = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr')

links = []

for index, player in enumerate(players):
    stats = []
    n = index+1
    players_dict = collections.OrderedDict()
    link = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[2]/a').get_attribute('href')
    links.append(link)
    print(n)
    print(link)
    stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[2]/a').text)
    stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(n)+']/td[3]/a').text)
    for i in [4,5,6,7,8,9,12,15,16,17,18,27,28,29,30]:
        stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(n)+']/td['+str(i)+']').text)
    for i in [10,11,13,14,19,20,21,22,23,24,25,26]:
        try:
            stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(n)+']/td['+str(i)+']/a').text)
        except selenium.common.exceptions.NoSuchElementException:
            stats.append(0.0)
    for i in range(28):
        players_dict[header[i]] = stats[i]
    writer.writerow(players_dict.values())

csv_file.close()

driver.close()
