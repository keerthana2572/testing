from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#to maximize the window
driver.maximize_window()
driver.get("http://localhost/Online_Hotel_Reservation/")
arrow=driver.find_element(By.XPATH,'//*[@id="myCarousel"]/a[2]/span[1]')
arrow.click()
time.sleep(10)
button=driver.find_element(By.XPATH,'//*[@id="myCarousel"]/ol/li[3]')
button.click()
time.sleep(1)
driver.close()
