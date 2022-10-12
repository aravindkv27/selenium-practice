from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


PATH="D:\Projects\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://www.udemy.com/")
print(driver.title)

search = driver.find_element(By.XPATH, "//input[@class='udlite-text-input udlite-text-input-small udlite-text-sm udlite-search-form-autocomplete-input js-header-search-field']")
# search.click
# search.clear()
search.send_keys("Web Development") #in search camera is searched
search.send_keys(Keys.RETURN)

time.sleep(5)
# driver.quit()