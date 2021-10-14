from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH="/home/aravind/Featurepreneur/chromedriver"
driver=webdriver.Chrome(PATH)

def wiki():
    driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")
    print(driver.title)
    
    wiki_con=driver.find_element_by_class_name("toctext")
    wiki_con.click()


    # sel_dev=driver.find_element_by_class_name("url")
    # sel_dev.click()

    time.sleep(10)
    driver.quit()

if __name__=='__main__':
    wiki()