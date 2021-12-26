from tests.base_test import BaseTest
from configurations.config import TestData, Test_Data_009
from pages.login_page import LoginPage
from pages.create_tag_page import CreateTagPage 
from utils.customLogger import LogGeneration
import time 


class Test_009_CreateTag(BaseTest):
    username = TestData.username
    password = TestData.password
    homepage_url = Test_Data_009.homepage_url
    logger= LogGeneration.loggen()

    def test_create_tag(self):
        self.logger.info("*****Create Tag Test******")

        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull*****")
        time.sleep(5)
        
        self.obj = CreateTagPage(self.driver)
        
        self.obj.collapse_other_menu()
        time.sleep(3)
        self.obj.click_add_tag_button()
        time.sleep(3)
        self.obj.click_no_thanks_button()
        time.sleep(3)
        is_redirect_to_home_page = self.obj.is_home_page(self.homepage_url)
        
        if is_redirect_to_home_page == True:
            self.logger.info("*****Redirected to home page successfully******")
            self.logger.info("*****Create Tag Test Passed******")
            assert True
        else:
            self.logger.info("*****Redirected to home page failed******")
            self.logger.info("*****Create Tag Test failed******")
            assert False






    
        
