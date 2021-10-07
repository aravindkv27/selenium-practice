import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH="/home/aravind/Featurepreneur/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://techwithtim.net")

print(driver.title)

search=driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# try:
#     main=WebDriverWait(driver,10).until(
#         EC.presence_of_elements_located((By.ID,"main"))
#     )
    
# except:
#     driver.quit()


# print(main.txt)

time.sleep(10)
driver.quit()