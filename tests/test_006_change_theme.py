from tests.base_test import BaseTest
from configurations.config import TestData, Test_Data_005
from pages.login_page import LoginPage
from pages.change_theme_page import ChangeThemePage
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

        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull ****")
        time.sleep(5)
        
        self.logger.info("****Started Adding Items to List******")
        
        self.obj = ChangeThemePage(self.driver)

        self.obj.click_settings_icon()
        time.sleep(2)
        self.obj.click_theme_button()
        time.sleep(2)

        self.obj.select_dark_theme()
        time.sleep(5)

        is_dark_theme_selected = self.obj.dark_theme_is_selected()
        
        if is_dark_theme_selected == True:
            print("Theme changed to dark")
            self.logger.info("*****Dark Theme Selected successfully******")
        else:
            self.logger.info("*****Dark Theme Selection Test Failed******")
            assert False
        
        self.obj.select_light_theme()
        time.sleep(4)

        is_light_theme_selected = self.obj.light_theme_is_selected()

        if is_light_theme_selected == True:
            print("Theme changed to light")
            self.logger.info("*****Theme Chnaged to Light successfully******")
            self.logger.info("*****Change Theme Test passed******")
            assert True
        else:
            self.logger.info("*****Light Theme Selection Test Failed******")
            self.logger.info("*****Change Theme Test failed******")
            assert False

        

