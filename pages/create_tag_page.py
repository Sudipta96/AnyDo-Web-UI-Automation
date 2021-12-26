from utils.locators import *
from pages.base_page import BasePage
import time


class  CreateTagPage(BasePage):
    def __init__(self, driver):
        self.locator = Createtag
        super(CreateTagPage, self).__init__(driver)
    
    def collapse_other_menu(self):
        self.find_element(*self.locator.collapse_shortcuts).click()
        time.sleep(2)
        self.find_element(*self.locator.collapse_list_shortcuts).click()


    def click_add_tag_button(self):
        self.wait_element(*self.locator.add_tag_icon)
        element = self.find_element(*self.locator.add_tag_icon)
        element.click()


    def click_no_thanks_button(self):
        self.find_element(*self.locator.no_thanks_button).click()


    def is_home_page(self, home_page_url):
        home_page = False
        if self.get_url() == home_page_url:
            home_page = True
        return home_page

    


    


