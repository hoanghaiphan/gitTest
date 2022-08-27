#scraping example
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import randrange
import pandas as pd
import time
#driver = webdriver.Chrome('C:/Users/NA1696/Downloads/chromedriver_win32_76/chromedriver')
#driver.get('http://info.nowgoal.com/en/SubLeague/2010-2011/9/132.html')

servicePath=Service('C:/Users/hoanghai/Documents/2022Python/chromedriver.exe')
driver = webdriver.Chrome(service=servicePath)

#season = ['2010-2011', '2011-2012', '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019']
season = ['2020-2021']
#Loop through seasons
for s in season:
#     driver = webdriver.Chrome('C:/Users/Pc/Downloads/2021Python/webScraping/chromedriver')
#     driver = webdriver.Chrome(service=servicePath)
    driver.get('https://www.nowgoal.pro/football/database/schedule-9-' + s)
    #driver.get('http://info.nowgoal.com/en/SubLeague/' + s + '/33.html')
    OddsRecord = pd.DataFrame(columns=['Round','Hometeam', 'Scorehome', 'Scoreaway','Awayteam','Home','Draw','Away','Date','Status'])

#     round_no = driver.find_elements_by_class_name("rounds")
    round_no = driver.find_elements(By.CLASS_NAME,'rounds')
    #Loop through rounds
    for i in round_no:
        Round = i.text
        i.click()
        #match_no = driver.find_elements_by_xpath("//*[contains(@title,'Odds')]")
        match_no = driver.find_elements_by_xpath("//*[contains(@title,'Odds')]")
        for j in match_no:
            while (len(driver.window_handles) < 2):
                j.click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])

            hometeam = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td/span/a")[0].text
            homescore = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td[2]/div/div/div")[0].text
            awayscore = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td[2]/div/div/div[3]")[0].text
            awayteam = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td[3]/span/a")[0].text

            #navigate to 365
            menu_no = driver.find_elements_by_xpath("//*[contains(@class,'mintopnav v2')]/li[4]")
            menu_no[0].click()
            menu_no = driver.find_elements_by_xpath("//*[contains(@id,'comBtn_8')]")
            menu_no[0].click()

            #get odd from table
            Home = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[3]")
            Draw = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[4]")
            Away = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[5]")
            Date = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[6]")
            Status = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[7]")
            #table_no = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*")

            for k in range(1,len(Home)):
                OddsRecord.loc[len(OddsRecord)] = [Round, hometeam, homescore, awayscore, awayteam, Home[k].text, Draw[k].text, Away[k].text, Date[k].text, Status[k].text]

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    #OddsRecord.to_csv('Bundesliga2_' + s + '.csv')
    OddsRecord.to_csv('Bundesliga2_' + s + '.csv')
print("Done!")

