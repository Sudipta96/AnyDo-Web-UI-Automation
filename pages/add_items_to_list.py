from utils.locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys 
import time


class AddItemsToListPage(BasePage):

    def __init__(self, driver):
        self.locator = AddItemToList
        super(AddItemsToListPage, self).__init__(driver)
    
    def collapse_list_menu(self):
        self.wait_element(*self.locator.collapse_shortcut_icon)
        self.find_element(*self.locator.collapse_shortcut_icon).click()
    
    def click_list_item(self):
        element = self.find_element(*self.locator.listname)
        self.driver.execute_script("arguments[0].click();", element)
    
    def enter_taskname(self, task_list):
        for item in task_list:
            self.find_element(*self.locator.add_task_input).clear()
            self.find_element(*self.locator.add_task_input).send_keys(item)
            self.find_element(*self.locator.add_task_input).send_keys(Keys.ENTER)
            time.sleep(1)

    def check_items_visibility(self, task_list):
        print("check items_visibility() called...")
        flag = False
        list_items_box = self.find_element(*self.locator.list_items_box)
        for item in task_list:
            if item in list_items_box.text:
                flag = True
        return flag
    

    


