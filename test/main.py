from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#to maximize the window
driver.maximize_window()

driver.get("http://localhost:3000/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(driver.title)
time.sleep(5)
driver.get("http://localhost:3000/tableReservation")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
searchbox=driver.find_element(By.XPATH,"/html/body/div[1]/form/p[1]/input")
searchbox.send_keys('Restaurant')
phone=driver.find_element(By.XPATH,"/html/body/div[1]/form/p[2]/input")
phone.send_keys('3453893832')
adults=driver.find_element(By.ID,"adults")
adults.send_keys('2')
child=driver.find_element(By.ID,'children')
child.send_keys('1')
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
print(driver.title)
driver.close()