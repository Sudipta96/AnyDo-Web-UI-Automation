from utils.locators import *
from pages.base_page import BasePage
from configurations.config import TestData
from selenium.webdriver.common.keys import Keys 


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver) 
        self.driver.get(TestData.baseURL)
        
    def continue_with_email(self):
        self.wait_element(*self.locator.continue_with_email)
        self.find_element(*self.locator.continue_with_email).click()
    
    def enter_email(self, email):
        self.find_element(*self.locator.email_input).clear()
        self.find_element(*self.locator.email_input).send_keys(email)
        self.find_element(*self.locator.email_input).send_keys(Keys.ENTER)
        

    def enter_password(self, password):
        self.find_element(*self.locator.password_input).clear()
        self.find_element(*self.locator.password_input).send_keys(password)
    

    def click_login_button(self):
        self.find_element(*self.locator.signin_btn).click()
    
    def login(self, email, password):
        self.continue_with_email()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()


    