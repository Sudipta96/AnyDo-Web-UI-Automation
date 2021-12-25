import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.readProperties import ReadConfig
from utils.customLogger import LogGeneration


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

import time 

@pytest.mark.usefixtures("init_driver")
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger= LogGeneration.loggen()


    def test_login(self):
        self.logger.info("****Started Login Test****")
        # self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.implicitly_wait(10)

        self.lp=LoginPage(self.driver)
        # time.sleep(5)
        self.lp.continue_with_email()
        self.lp.enter_email(self.username)
        time.sleep(1)
        self.lp.enter_password(self.password)
        time.sleep(1)
        self.lp.click_login_button()
        time.sleep(4)

        title= self.driver.title

        if title=="Any.do":
            self.lp.click_logout_button()
            self.logger.info("****Login test passed ****")
            # self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            # self.driver.close()
            assert False

