from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#to maximize the window
driver.maximize_window()
driver.get("http://localhost/hotel_reservation/")
page=driver.find_element(By.XPATH,"//*[@id=menu]/li[6]/a")
page.click()
if driver.title=="Hotel Iris":
    print("navigation successful")
else:
    print ("navigation failed")
driver.close()