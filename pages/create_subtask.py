from pages.create_task_page import CreateTaskPage
from tests.base_test import BaseTest
from utils.locators import *
from pages.base_page import BasePage




class CreateSubTaskPage(BasePage):

    def __init__(self, driver):
        self.locator = CreateSubTaskLocators
        super(CreateSubTaskPage, self).__init__(driver)  # Python2 version
    
    def get_task_item(self, taskname):
        self.find_element(*self.locator.task_item).click()
    
    def click_add_subtask_button(self):
        self.wait_element(*self.locator.subtask_btn)
        self.find_element(*self.locator.subtask_btn).click()
    
    def enter_subtask(self, subtask_name):
        subtask_input_div = self.find_element(*self.locator.add_subtask_input)
        input_field = subtask_input_div.find_elements(By.TAG_NAME, "input")[0]
        input_field.clear()
        input_field.send_keys(subtask_name)

        
    def subtask_item_visible(self):
        subtask_item = self.find_element(*self.locator.subtask_item).get_attribute('value')
        return subtask_item

        
   
        
    

    