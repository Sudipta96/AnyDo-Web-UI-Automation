from pages.login_page import LoginPage
from pages.create_task_page import CreateTaskPage
from tests.base_test import BaseTest
from utils.customLogger import LogGeneration
from configurations.config import TestData, Test_Data_001
import time 



class Test_001_Create_Task(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()

    taskname = Test_Data_001.taskname
        
    def test_create_task(self):
        self.logger.info("*****Started Create Task Test******")
        
        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull ****")

        self.logger.info("****Started creating task ****")
        self.create_task_obj = CreateTaskPage(self.driver)
        self.create_task_obj.click_create_task_btn()
        self.create_task_obj.enter_task_name(self.taskname)
        self.create_task_obj.click_add_task_btn()
        time.sleep(5)
        
        task_list = self.create_task_obj.get_task_list()


        if self.taskname in task_list:
            self.logger.info("*****Create Task Test passed******")
            assert True
        else:
            self.logger.error("*****Create Task Test failed******")
            self.save_screenshot("test_create_task.png")
            assert False