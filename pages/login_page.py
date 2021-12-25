from utils.locators import *
from pages.base_page import BasePage
from configurations.config import TestData

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version
        self.driver.get(TestData.baseURL)
        
    def continue_with_email(self):
        self.wait_element(*self.locator.continue_with_email)
        self.find_element(*self.locator.continue_with_email).click()
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.continue_with_email_btn))).click()
        # self.wait_element(*self.locator.continue_with_email_btn)
        # self.find_element(*self.locator.continue_with_email_btn).click()
        # self.element.click()

    def enter_email(self, email):
        # self.wait_element(*self.locator.email_input)
        # self.find_element(*self.locator.email_input).send_keys(email)
        print("enter_email() called... ")

        # self.continue_with_email = '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]/div/div[1]'
        # self.wait_element(*self.locator.continue_with_email)
        # self.find_element(*self.locator.continue_with_email).click()
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.continue_with_email))).click()

        self.find_element(*self.locator.email_input).clear()
        self.find_element(*self.locator.email_input).send_keys(email)
        self.find_element(*self.locator.email_input).send_keys(Keys.ENTER)
        

    def enter_password(self, password):
        # self.wait_element(*self.locator.password_input)
        # self.find_element(*self.locator.password_input).send_keys(password)
        self.find_element(*self.locator.password_input).clear()
        self.find_element(*self.locator.password_input).send_keys(password)
    

    def click_login_button(self):
        self.find_element(*self.locator.signin_btn).click()
        # self.find_element(By.XPATH, self.signin_btn).click()
    
    def login(self, email, password):
        self.continue_with_email()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def click_logout_button(self):
        # self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        self.wait_element(*self.locator.settings_icon_xpath)
        self.find_element(*self.locator.settings_icon_xpath).click()
        self.find_element(*self.locator.my_profile_xpath).click()
        self.find_element(*self.locator.sign_out_xpath).click()
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.my_profile_xpath))).click()
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.sign_out_xpath))).click()

    