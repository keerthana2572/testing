import unittest
import time
from selenium.webdriver.common.by import By

class FirstTest(unittest.TestCase):

    def test_home(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver import ActionChains
        import time
        from selenium.webdriver.common.keys import Keys
        driver = webdriver.Chrome()
        # to maximize the window
        driver.maximize_window()
        driver.get("http://localhost/Online_Hotel_Reservation/")
        arrow = driver.find_element(By.XPATH, '//*[@id="myCarousel"]/a[2]/span[1]')
        arrow.click()
        time.sleep(10)
        button = driver.find_element(By.XPATH, '//*[@id="myCarousel"]/ol/li[3]')
        button.click()


    def test_reserve(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("http://localhost/Online_Hotel_Reservation/add_reserve.php?room_id=1")
        driver.maximize_window()
        pass_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[1]/input')
        pass_name.send_keys('Pooja')
        time.sleep(0.5)
        m_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[2]/input')
        m_name.send_keys('.')
        time.sleep(0.5)
        l_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[3]/input')
        l_name.send_keys('A')
        time.sleep(0.5)
        address = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[4]/input')
        address.send_keys('bangalore')
        time.sleep(0.5)
        contact = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[5]/input')
        contact.send_keys('999348232')
        time.sleep(0.5)
        date = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[6]/input')
        date.send_keys('01/09/2023')
        time.sleep(1)
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[7]/button')
        button.click()
        assert driver.title=='Confirmation'

        driver.quit()


if __name__=="__main__":
    unittest.main()