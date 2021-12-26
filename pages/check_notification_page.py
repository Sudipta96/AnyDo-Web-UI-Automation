from utils.locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys 
import time


class CheckNotificationPage(BasePage):

    def __init__(self, driver):
        self.locator = CheckNotification
        super(CheckNotificationPage, self).__init__(driver)
    
    def click_notification_button(self):
        self.find_element(*self.locator.notification_button).click()

    def click_notification_update_button(self):
        self.find_element(*self.locator.notification_updates_button).click()

    def does_popup_menu_visible(self):
        notification_menu = self.find_element(*self.locator.notification_menu)
        return bool(notification_menu)    

    
    