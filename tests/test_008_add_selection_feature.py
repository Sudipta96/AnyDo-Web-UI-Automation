from tests.base_test import BaseTest
from configurations.config import TestData
from pages.login_page import LoginPage
from pages.add_selection_feature import AddSelectionFeaturePage 
from utils.customLogger import LogGeneration
from selenium.webdriver.common.keys import Keys
import time 


class Test_008_AddSelectionFeature(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()

    def test_add_selection_feature(self):
        self.logger.info("*****Add Selection Feature Test******")

        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull*****")
        time.sleep(5)
        
        self.obj = AddSelectionFeaturePage(self.driver)

        self.obj.collapse_list_menu()
        time.sleep(2)
        self.obj.click_list_item()
        time.sleep(2)
        
        self.obj.click_more_option_button()
        time.sleep(2)
        self.obj.click_multiple_selection_button()
        is_visible = self.obj.is_taskbatch_toolbar_visible()

        if is_visible == True:
            self.obj.click_items_of_task_list()
            time.sleep(2)
            total_selected_items = self.obj.task_selected_items_count()
            if int(total_selected_items) > 1:
                self.logger.info("*****More than one task item have selected successfully******")
                self.logger.info("*****Add Selection Feature Test Passed******")
                assert True
            else:
                self.logger.info("*****Add Selection Feature Test failed******")
                assert False
        else:
            self.logger.info("*****Taskbatch Toolbar is not visible******")
            self.logger.info("*****Add Selection Feature Test failed******")
            assert False








    
        
