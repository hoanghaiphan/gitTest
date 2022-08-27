# Old API New API
# find_element_by_id(‘id’) find_element(By.ID, ‘id’)
# find_element_by_name(‘name’) find_element(By.NAME, ‘name’)
# find_element_by_xpath(‘xpath’) find_element(By.XPATH, ‘xpath’)
# find_element_by_link_text(‘link_text’) find_element(By.LINK_TEXT, ‘link_text’)
# find_element_by_partial_link_text(‘partial_link_text’) find_element(By.PARTIAL_LINK_TEXT, ‘partial_link_text’)
# find_element_by_tag_name(‘tag_name’)find_element(By.TAG_NAME, ‘tag_name’)
# find_element_by_class_name(‘class_name’)find_element(By.CLASS_NAME, ‘class_name’)
# find_element_by_css_selector(‘css_selector’)find_element(By.CSS_SELECTOR, ‘css_selector’)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import randrange
import time
from datetime import datetime

# driver = webdriver.Chrome('C:/Users/hoanghai/Documents/2022Python/chromedriver.exe')

s=Service('C:/Users/hoanghai/Documents/2022Python/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://paulgraham.com/articles.html')
time.sleep(5)
print("I waited for 5 seconds.")
# links=driver.find_elements(By.NAME,"a")
# links=driver.find_elements(By.XPATH,'*//a[@href=*]')
links=driver.find_elements(By.XPATH,'//*[contains(@href,"html")]')

# selectlink=Select(links)

# search_box = driver.find_element("name", "q")

i=randrange(1,len(links))
#
articleName = links[i].text
links[i].click()

f=open("readList.txt","a")
f.write("\n")
readTime = datetime.now()
f.write(str(readTime))
f.write(": ")
f.write(articleName)
f.close()

