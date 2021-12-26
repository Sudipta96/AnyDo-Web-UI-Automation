from utils.locators import *
from pages.base_page import BasePage


class CreateTaskPage(BasePage):

    def __init__(self, driver):
        self.locator = CreateTaskLocators
        super(CreateTaskPage, self).__init__(driver) 
    
    def click_create_task_btn(self):
        self.wait_element(*self.locator.create_task_button)
        self.find_element(*self.locator.create_task_button).click()

    def enter_task_name(self, taskname):
        self.find_element(*self.locator.enter_task_name_input).clear()
        self.find_element(*self.locator.enter_task_name_input).send_keys(taskname)

        
    def click_add_task_btn(self):
        self.find_element(*self.locator.add_task_btn).click()

    def get_task_list(self):
        self.wait_element(*self.locator.task_list)
        return self.find_element(*self.locator.task_list).text

    



        
    

    