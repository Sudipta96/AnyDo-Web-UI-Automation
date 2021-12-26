from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configurations.config import TestData


class BasePage:
    def __init__(self, driver, base_url=TestData.baseURL):
        self.base_url = base_url
        self.driver = driver
    

    def find_element(self, *by_locator):
        return self.driver.find_element(*by_locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def zoom_out_window(self):
        self.driver.execute_script("document.body.style.zoom='90%'")
    
    def zoom_in_window(self):
        self.driver.execute_script("document.body.style.zoom='100%'")

    def wait_element(self, *by_locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        except TimeoutException:
            print("ELEMENT IS NOT FOUND WITHIN GIVEN TIME")
            self.driver.quit()