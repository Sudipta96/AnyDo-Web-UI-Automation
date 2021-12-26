from selenium.webdriver.common.keys import Keys
from utils.locators import *
from pages.base_page import BasePage
import time



class CreateSubTaskPage(BasePage):
    def __init__(self, driver):
        self.locator = CreateSubTaskLocators
        super(CreateSubTaskPage, self).__init__(driver)
    
    def click_next_week_button(self):
        self.find_element(*self.locator.next_seven_days_button).click()
    
    def click_task_item(self):
        self.wait_element(*self.locator.task_item)
        self.find_element(*self.locator.task_item).click()

   
    def scroll_task_dialog(self):
        dialog = self.find_element(*self.locator.task_dialog)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", dialog)
        
    
    def click_add_subtask_button(self):
        self.wait_element(*self.locator.add_subtask_btn)
        time.sleep(5)
        self.find_element(*self.locator.add_subtask_btn).click()
    
    def enter_subtask(self, subtask_name):
        subtask_input_div = self.find_element(*self.locator.add_subtask_input)
        input_field = subtask_input_div.find_elements(By.TAG_NAME, "input")[0]
        input_field.clear()
        input_field.send_keys(subtask_name)
        input_field.send_keys(Keys.ENTER)

        
    def subtask_item_visible(self):
        subtask_item = self.find_element(*self.locator.subtask_item).get_attribute('value')
        return subtask_item

        
   
        
    

    