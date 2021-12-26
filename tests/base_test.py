import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from configurations.config import TestData

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def save_screenshot(self, filename):
        self.driver.save_screenshot(".\\Screenshots\\" + filename)
    
    def move_backward(self):
        self.driver.back()
    
    def scroll_window(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    def zoom_out_window(self, url):
        # self.driver.get(url)
        self.driver.execute_script("document.body.style_zoom='70%'")
        # self.driver.send_keys(Keys.CONTROL, '-')
    
    def zoom_in_window(self):
        self.driver.execute_script("document.body.style_zoom='90%'")
        # self.driver.send_keys(Keys.CONTROL, '+')
        

    