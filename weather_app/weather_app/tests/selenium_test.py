"""
    This Module is for a positive and a negative test of the web page,
    if the parameter entered and sent to the API returns what we expect
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

url = "http://10.10.1.3/"

 
class LocationPage(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.get(url)
       username = self.driver.find_element(By.ID, "username")
       password = self.driver.find_element(By.ID,"password")
       username.send_keys("ziv")
       password.send_keys("123456")
       submit = self.driver.find_element(By.CLASS_NAME, "btn-medium")
       submit.click()
    #  get_url = self.driver.current_url
    #  assert "home" in get_url
    
    def test_positive(self):
        input = self.driver.find_element(By.ID, "location")
        input.send_keys("Haifa")
        submit = self.driver.find_element(By.CLASS_NAME, "btn-medium")
        submit.click()
        time.sleep(2)
        title = self.driver.find_element(By.CLASS_NAME, "city_title")
        print(title.text)
        assert "Haifa" == title.text
        
    def test_negative(self):
            input = self.driver.find_element(By.ID, "location")
            input.send_keys("blablablo")
            submit = self.driver.find_element(By.CLASS_NAME, "btn-medium")
            submit.click()
            time.sleep(2)
            title = self.driver.find_element(By.CLASS_NAME, "city_title")
            print(title.text)
            assert "Texas" == title.text
        
        
if __name__ == '__main__':
    unittest.main()
                
        