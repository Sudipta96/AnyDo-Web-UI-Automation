from tests.base_test import BaseTest
from configurations.config import TestData
from pages.login_page import LoginPage
from pages.change_theme_page import ChangeThemePage
from utils.customLogger import LogGeneration
import time 


class Test_005_ChangeTheme(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()

    def test_change_theme(self):
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

        

