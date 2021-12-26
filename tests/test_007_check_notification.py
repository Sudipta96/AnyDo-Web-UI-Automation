from tests.base_test import BaseTest
from configurations.config import TestData
from pages.login_page import LoginPage
from pages.check_notification_page import CheckNotificationPage
from utils.customLogger import LogGeneration
import time 


class Test_007_CheckNotification(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()

    def test_check_notfication(self):
        self.logger.info("*****Check Notification Test******")

        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull*****")
        time.sleep(5)
        
        self.logger.info("****Started Checking Notification******")
    
        self.obj = CheckNotificationPage(self.driver)

        self.obj.click_notification_button()
        time.sleep(2)
        self.obj.click_notification_update_button()

        is_popmenu_visible = self.obj.does_popup_menu_visible()

        if is_popmenu_visible == True:
            self.logger.info("*****Popup menu is visible******")
            self.logger.info("*****Check Notification Test passed******")
            assert True
        else:
            self.logger.info("*****Popup menu is not visible ******")
            self.logger.info("*****Check Notification Test failed******")
            assert False

        

