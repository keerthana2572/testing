from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#to maximize the window
driver.maximize_window()
driver.get("http://localhost/Online_Hotel_Reservation/admin/room.php")
username=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/form/div[1]/input")
username.send_keys('Admin')
password=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/form/div[2]/input")
password.send_keys('admin')
btn=driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/form/div[3]/button').click()
