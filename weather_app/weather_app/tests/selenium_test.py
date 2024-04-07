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
    
    def find_location(self, location):
        input = self.driver.find_element(By.ID, "location")
        input.send_keys(location)
        submit = self.driver.find_element(By.CLASS_NAME, "btn-medium")
        submit.click()
        return self.driver
    
    def test_positive(self):
        assert self.find_location("Haifa").find_element(By.CLASS_NAME, "city_title")
        # .text == "Haifa"
        
    def test_negative(self):
            assert self.find_location("blablablo").find_element(By.CLASS_NAME, "city_title")
        
        
if __name__ == '__main__':
    unittest.main()
                
        