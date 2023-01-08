from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#to maximize the window
driver.maximize_window()
driver.get("http://localhost//add_reserve.php?room_id=1")

pass_name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[1]/input')
pass_name.send_keys('Pooja')
time.sleep(0.5)
m_name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[2]/input')
m_name.send_keys('.')
time.sleep(0.5)
l_name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[3]/input')
l_name.send_keys('A')
time.sleep(0.5)
address=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[4]/input')
address.send_keys('bangalore')
time.sleep(0.5)
contact=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[5]/input')
contact.send_keys('999348232')
time.sleep(0.5)
date=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[6]/input')
date.send_keys('22/01/2023')
time.sleep(1)
button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[7]/button')
button.click()
title=driver.title;
print(title)
time.sleep(5)
if(title == 'Confirmation'):
    print('Reservation Successful')
else:
    print("Reservation Unsuccesful")
driver.close()

