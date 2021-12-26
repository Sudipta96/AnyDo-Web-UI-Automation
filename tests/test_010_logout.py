from tests.base_test import BaseTest
from configurations.config import TestData, Test_Data_010
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from utils.customLogger import LogGeneration
import time 


class Test_010_Logout(BaseTest):
    username = TestData.username
    password = TestData.password
    sign_in_page_title = Test_Data_010.sign_in_page_title
    logger= LogGeneration.loggen()

    def test_logout(self):
        self.logger.info("*****Logout Test******")

        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull*****")
        time.sleep(5)
        
        self.obj = LogoutPage(self.driver)

        self.obj.logout()

        title = self.obj.get_title()

        if title == self.sign_in_page_title:
            self.logger.info("****Logout successfull*****")
            self.logger.info("****Test 010 Logout passed*****")
            assert True
        else:
            self.logger.info("****Logout failed*****")
            self.logger.info("****Test 010 Logout failed*****")
            assert False


        
       






    
        
