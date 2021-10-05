import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://www.javatpoint.com/selenium-python")
print(driver.title)



try:
    summary=WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"menu"))
    )
    print(summary.text)
    
except:
    driver.quit()

# time.sleep(10)
driver.quit()