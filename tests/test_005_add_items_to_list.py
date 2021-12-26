from tests.base_test import BaseTest
from configurations.config import TestData, Test_Data_005
from pages.login_page import LoginPage
from pages.add_items_to_list import AddItemsToListPage
from utils.customLogger import LogGeneration
from selenium.webdriver.common.keys import Keys
import time 


class Test_005_AddItemsToList(BaseTest):
    username = TestData.username
    password = TestData.password
    listname = Test_Data_005.listname
    list_items = Test_Data_005.list_items
    logger= LogGeneration.loggen()

    def test_add_items_to_list(self):
        self.logger.info("*****Add Items To List Test******")
        # time.sleep(20)
        
        # self.zoom_out_window()
        # time.sleep(5)

        # assert True

        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull ****")
        time.sleep(5)
        
        self.logger.info("****Started Adding Items to List******")
        self.obj = AddItemsToListPage(self.driver)
                
        self.obj.collapse_list_menu()
        time.sleep(3)
        
        self.obj.zoom_out_window()
        time.sleep(4)

        self.obj.click_list_item()

        self.obj.enter_taskname(self.list_items)

        items_visibility = self.obj.check_items_visibility(self.list_items)

        if items_visibility == True:
            self.logger.info("****Adding Items to List passed******")
            assert True
        else:
            self.logger.info("****Adding Items to List failed******")
            assert False
        



