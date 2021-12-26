from tests.base_test import BaseTest
from configurations.config import TestData, Test_Data_004
from pages.login_page import LoginPage
from pages.create_list_page import CreateListPage
from utils.customLogger import LogGeneration
import time 


class Test_004_Create_List(BaseTest):
    username = TestData.username
    password = TestData.password
    listname = Test_Data_004.listname
    logger= LogGeneration.loggen()

    def test_create_list(self):
        self.logger.info("*****Started Create SubTask Test******")
        
        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull ****")

        self.logger.info("****Started Creating List******")
        time.sleep(4)
        self.create_list_obj = CreateListPage(self.driver)
        self.create_list_obj.click_add_list_icon()
        time.sleep(2)
        self.create_list_obj.enter_list_name(self.listname)
        self.create_list_obj.click_create_list_button()
        time.sleep(2)
        assert self.create_list_obj.does_list_item_created(self.listname)
        # assert True
        # self.logger.info("**** Test Create List passed******")
        



