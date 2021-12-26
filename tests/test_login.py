from tests.base_test import BaseTest
from configurations.config import TestData
from pages.login_page import LoginPage
from utils.customLogger import LogGeneration
import time 


class Test_Login(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()


    def test_login(self):
        self.logger.info("****Started Login Test****")

        self.obj= LoginPage(self.driver)
        time.sleep(5)
        self.obj.continue_with_email()
        self.obj.enter_email(self.username)
        time.sleep(1)
        self.obj.enter_password(self.password)
        time.sleep(1)
        self.obj.click_login_button()
        time.sleep(4)

        title = self.obj.get_title()

        if title == "Any.do":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False

