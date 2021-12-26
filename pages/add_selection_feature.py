from utils.locators import *
from pages.base_page import BasePage
import time


class AddSelectionFeaturePage(BasePage):

    def __init__(self, driver):
        self.locator = AddSelectionFeature
        super(AddSelectionFeaturePage, self).__init__(driver)
    
    def collapse_list_menu(self):
        self.wait_element(*self.locator.collapse_shortcut_button)
        self.find_element(*self.locator.collapse_shortcut_button).click()
    
    def click_list_item(self):
        element = self.find_element(*self.locator.list_item)
        self.driver.execute_script("arguments[0].click();", element)

    def click_more_option_button(self):
        self.find_element(*self.locator.more_options_icon).click()
    
    def click_multiple_selection_button(self):
        self.find_element(*self.locator.mutiple_selection_button).click()
    
    def is_taskbatch_toolbar_visible(self):
        element = self.find_element(*self.locator.taskbatchtoolbar)
        return bool(element)
    
    def click_items_of_task_list(self):
        task_list_container = self.find_element(*self.locator.task_list_container)
        items_list = task_list_container.find_elements(By.XPATH, '//div[@class="TaskList__taskContainer"]')
        for item in items_list:
            item.click()
            time.sleep(1)

    def task_selected_items_count(self):
        element = self.find_element(*self.locator.task_selected_items_count).text
        return int(element)

    
    
   

    


