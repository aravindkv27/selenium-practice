from selenium import webdriver

PATH="/home/aravind/Featurepreneur/chromedriver"

driver=webdriver.Chrome(PATH)
driver.get("https://selenium-python.readthedocs.io/getting-started.html")

driver.close()