from utils.locators import *
from pages.base_page import BasePage




class LogoutPage(BasePage):

    def __init__(self, driver):
        self.locator = LogoutLocators
        super(LogoutPage, self).__init__(driver) 
    
    def logout(self):
        self.wait_element(*self.locator.settings_icon)
        self.find_element(*self.locator.settings_icon).click()
        self.find_element(*self.locator.my_profile_button).click()
        self.find_element(*self.locator.sign_out_button).click()
    

        
   
        
    

    