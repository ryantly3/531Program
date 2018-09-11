from selenium import webdriver
import selenium
import collections
import time
import csv

driver = webdriver.Chrome()

driver.get('https://stats.nba.com/players/boxscores/?sort=PLAYER_NAME&dir=-1')
#driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()
time.sleep(20)

csv_file = open('gamelogs.csv', 'w')
writer = csv.writer(csv_file)
header=['PLAYER', 'TEAM', 'MATCH UP', 'DATE', 'W/L', 'MIN', 'PTS', 'FG%', '3P%', 'FTM', 'FTA', 'FT%', 'PF', '+/-', 'FGM', 'FGA', '3PM', '3PA', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'TOV']
writer.writerow(header)

games = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr')

for i in range(523):
    print(i)
    for index, game in enumerate(games):
        stats = []
        n = index+1
        games_dict = collections.OrderedDict()

        stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[2]/table/tbody/tr['+str(n)+']/td/a').text)
        for i in [2,3,4]:
            stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(n)+']/td['+str(i)+']/a').text)
        for i in [5,6,7,8,11,15,16,17,25,26]:
            try:
                stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(n)+']/td['+str(i)+']').text)
            except selenium.common.exceptions.NoSuchElementException:
                stats.append('NaN')
        for i in [9,10,12,13,14,18,19,20,21,22,23,24]:
            try:
                stats.append(driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr['+str(n)+']/td['+str(i)+']/a').text)
            except selenium.common.exceptions.NoSuchElementException:
                stats.append(0.0)
        for i in range(26):
            games_dict[header[i]] = stats[i]
        writer.writerow(games_dict.values())
    driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]').click()
    time.sleep(5)

csv_file.close()

driver.close()
