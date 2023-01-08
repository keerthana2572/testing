from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#to maximize the window
driver.maximize_window()
driver.get("http://localhost/Online_Hotel_Reservation/admin/reserve.php")
username=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/form/div[1]/input")
username.send_keys('Admin')
password=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/form/div[2]/input")
password.send_keys('admin')
time.sleep(10)
btn=driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/form/div[3]/button').click()
driver.find_element(By.XPATH,'/html/body/div[1]/ul/li[3]/a').click()
time.sleep(10)
search=driver.find_element(By.XPATH,'//*[@id="table_filter"]/label/input')
search.send_keys('Pooja')
pending=driver.find_element(By.XPATH,'//*[@id="table"]/tbody/tr[1]/td[6]/center/a[1]')
pending.click()
roomno=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div[5]/input')
roomno.send_keys('100')
days=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div[6]/input')
days.send_keys('3')
extrabed=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div[7]/input')
extrabed.send_keys(1)
time.sleep(10)
submit=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/button')
submit.click()
time.sleep(10)
if driver.title=='CheckInConfirmation':
    print ('test passed')
else:
    print('test failed')
time.sleep(10)
driver.close()
