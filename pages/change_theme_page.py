from utils.locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys 
import time


class ChangeThemePage(BasePage):

    def __init__(self, driver):
        self.locator = ChangeTheme
        super(ChangeThemePage, self).__init__(driver)
    
    def click_settings_icon(self):
        self.find_element(*self.locator.settings_icon).click()

    def click_theme_button(self):
        self.find_element(*self.locator.theme_button).click()
    
    def select_dark_theme(self):
        self.find_element(*self.locator.dark_theme).click()

    def select_light_theme(self):
        self.find_element(*self.locator.light_theme).click()

    def dark_theme_is_selected(self):
        element = self.find_element(*self.locator.dark_theme)
        return element.is_selected()

    
    def light_theme_is_selected(self):
        element = self.find_element(*self.locator.light_theme)
        return element.is_selected()

    
    