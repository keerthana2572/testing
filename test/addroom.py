from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
room=driver.find_element(By.LINK_TEXT,'Room').click()
driver.find_element(By.LINK_TEXT,'Add Room').click()
select=Select(driver.find_element(By.CLASS_NAME,'form-control'))
select.select_by_visible_text('Standard')
price=driver.find_element(BY.XPATH,'/html/body/div[2]/div/div/div[2]/form/div[2]/input')
price.send_keys('1000')
photo=
time.sleep(10)

