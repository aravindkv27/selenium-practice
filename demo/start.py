from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://www.goibibo.com/flights/")

title=driver.title
print(title)



search=driver.find_element_by_id("gosuggest_inputSrc")
search.send_keys("Chennai (MAA)")
search.send_keys(Keys.RETURN)
search.click()

des=driver.find_element_by_id("gosuggest_inputDest")
des.send_keys("Mumbai (BOM)")
des.send_keys(Keys.RETURN)
des.click()

dep=driver.find_element_by_id("departureCalendar")



# time.sleep(10)

# driver.quit()