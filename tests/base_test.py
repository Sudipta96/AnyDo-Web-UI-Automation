import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.mark.usefixtures("init_driver")
class BaseTest:
    
    def save_screenshot(self, filename):
        self.driver.save_screenshot(".\\Screenshots\\" + filename)
