from pages.create_task_page import CreateTaskPage
from utils.locators import *
from pages.base_page import BasePage

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys 



class CreateTaskNotesPage(CreateTaskPage):

    def __init__(self, driver):
        self.locator = CreateTaskLocators
        super(CreateTaskNotesPage, self).__init__(driver)  # Python2 version
    
    def enter_notes_name(self, notes):
        print("------enter_notes_name() called...")
        self.find_element(*self.locator.enter_notes_input).clear()
        self.find_element(*self.locator.enter_notes_input).send_keys(notes)
    
    def click_next_week_button(self):
        print("------click_next_week_button() called...")
        self.find_element(*self.locator.next_week_button).click()
    
    
    # def click_create_task_btn(self):
    #     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, create_task_xpath))).click()
    #     self.wait_element(*self.locator.create_task_button)
    #     self.find_element(*self.locator.create_task_button).click()

    # def enter_task_name(self, taskname):
    #     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, task_input_xpath))).send_keys(task_name)
    #     self.find_element(*self.locator.enter_task_name_input).clear()
    #     self.find_element(*self.locator.enter_task_name_input).send_keys(taskname)

        

    # def click_add_task_btn(self):
    #     # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, add_task_btn_xpath))).click()
    #     self.find_element(*self.locator.add_task_btn).click()

    # def get_task_list(self):
    #     return self.find_element(*self.locator.task_list).text

    



        
    

    