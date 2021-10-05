from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")

link=driver.find_element_by_link_text("Python Programming")
link.click()
# link=driver.find_element_by_link_text("Home")
# link.click()
# link=driver.find_element_by_class_name("Link-sc-1khjl8b-0 kdCHb Button-bwu3xu-0 uHxbQ")
# link.click()

try:
    element=WebDriverWait(driver,10).until(
        EC.presence_of_elements_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    element.click()
    

except:
    driver.quit()

time.sleep(10)
