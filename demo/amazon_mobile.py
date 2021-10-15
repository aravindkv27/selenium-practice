from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
import csv

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)
driver.maximize_window() #To maximize the web browser

data=[]



def amazon():
    driver.get("https://www.amazon.in/")
    title=driver.title
    data.append(title)
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

    #Print the about this item
    about=driver.find_element_by_id("feature-bullets").text
    
    
    data.append(about)
    time.sleep(5)
    
    #naviagate to home page
    navi=driver.find_element_by_id("nav-logo-sprites")
    navi.click()
    home=driver.title
    data.append(home)

#def data():
    


if __name__=="__main__":
    amazon()

    with open('/home/aravind/Featurepreneur/selenium-practice/demo/demo.txt','w') as file:
        for i in data:
            file.write("%s\n" % i)

    print(data)
    # data()
    # file=open('data.csv','w+',newline='')
    # with file:
    #     write=csv.writer(file)
    #     write.writerows(data)
    time.sleep(5)
    driver.quit() #quit the webpage