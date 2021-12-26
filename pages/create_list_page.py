from utils.locators import *
from pages.base_page import BasePage



class CreateListPage(BasePage):

    def __init__(self, driver):
        self.locator = CreateListLocators
        super(CreateListPage, self).__init__(driver)
    
    def click_add_list_icon(self):
        self.find_element(*self.locator.add_list_icon).click()
    
    def enter_list_name(self, listname):
        self.wait_element(*self.locator.add_list_input)
        self.find_element(*self.locator.add_list_input).clear()
        self.find_element(*self.locator.add_list_input).send_keys(listname)
    
    def click_create_list_button(self):
        self.find_element(*self.locator.create_list_button).click()
    
    def does_list_item_created(self, listname):
        list_category = self.find_element(*self.locator.list_category)
        list_items =  list_category.find_elements(By.TAG_NAME, "li")
        flag = False
        for item in list_items:
            if listname == item.text:
                flag = True
        return flag


    


