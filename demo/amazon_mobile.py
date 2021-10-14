from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)
driver.maximize_window() #To maximize the web browser

data=[]

def amazon():
    driver.get("https://www.amazon.in/")
    title=driver.title
    data.insert(0,title)
    print(title)

    #naviagte to mobiles
    amazon_pay=driver.find_element_by_link_text("Mobiles")
    amazon_pay.click()
    mob_title=driver.title
    print(mob_title)
    data.append(mob_title)

    time.sleep(3)

    #clicking Images
    mob=driver.find_element_by_xpath("//img[@alt='i11']")
    mob.click()

    time.sleep(5)
    #naviagate to home page
    navi=driver.find_element_by_id("nav-logo-sprites")
    navi.click()
    print(driver.title)

    time.sleep(5)
    driver.quit() #quit the webpage

if __name__=="__main__":
    amazon()
    print(data)