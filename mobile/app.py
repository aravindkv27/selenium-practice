from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mob_list=[]
PATH="/home/aravind/Featurepreneur/chromedriver"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.amazon.in/")

def ama_mob():
    
    #To print title
    home_title=driver.title
    print(home_title)

    #Search Mobiles
    search_mobiles=driver.find_element_by_id("twotabsearchtextbox")
    search_mobiles.clear()
    search_mobiles.send_keys("Moblies")
    search_mobiles.send_keys(Keys.RETURN)
    mob_title=driver.title
    print(mob_title)

    # #Scraping Mobile Names
    # titles=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2/a")
    # for title in titles:
    #     mob_list.append(title.text)

    i=0
    if i < 5:
        get_titles()
        i+=1

def get_titles():
        #Scraping Mobile Names
    titles=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2/a")
    for title in titles:
        mob_list.append(title.text)
    click_next=driver.find_element_by_xpath("//li[@class='a-last']")
    click_next.click()


def startpy():
       
    ama_mob() 

    with open('/home/aravind/Featurepreneur/selenium-practice/mobile/mobiles.txt','w') as file:
        for i in mob_list:
            file.write("%s\n" % i)
    time.sleep(5)
    driver.quit()

if __name__=="__main__":
    startpy()