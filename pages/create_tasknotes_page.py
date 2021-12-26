from pages.create_task_page import CreateTaskPage
from utils.locators import *
from pages.base_page import BasePage


class CreateTaskNotesPage(BasePage):

    def __init__(self, driver):
        self.locator = CreateTaskNotesLocators
        super(CreateTaskNotesPage, self).__init__(driver)

    def enter_notes_name(self, notes):
        self.find_element(*self.locator.enter_notes_input).clear()
        self.find_element(*self.locator.enter_notes_input).send_keys(notes)
    
    def click_next_week_button(self):
        self.wait_element(*self.locator.next_week_button)
        self.find_element(*self.locator.next_week_button).click()
    
    def click_personal_option_button(self):
        self.wait_element(*self.locator.personal_option_button)
        self.find_element(*self.locator.personal_option_button).click()  
    
    
                
    
   

    



        
    

    