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
        print("----does dark theme enabled")
        element = self.find_element(*self.locator.dark_theme)
        print(element.is_selected())
        print("----does dark theme end")
        return element.is_selected()

    
    def light_theme_is_selected(self):
        print("----does light theme enabled")
        element = self.find_element(*self.locator.light_theme)
        print(element.is_selected())
        print("----light theme end")
        return element.is_selected()

    
    