from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://www.amazon.in/")
title=driver.title  #to find the title

print(title)

search=driver.find_element_by_id("twotabsearchtextbox") #to search using id

search.clear()
search.send_keys("dslr") #in search camera is searched
search.send_keys(Keys.RETURN)


assert "No results are Found" not in driver.page_source

time.sleep(10)

driver.quit()
