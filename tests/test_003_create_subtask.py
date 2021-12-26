from pages.login_page import LoginPage
from pages.create_subtask_page import CreateSubTaskPage 
from pages.create_tasknotes_page import CreateTaskNotesPage
from tests.base_test import BaseTest
from utils.customLogger import LogGeneration
from configurations.config import TestData, Test_Data_003
import time 



class Test_003_Create_SubTask(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()

    taskname = Test_Data_003.taskname
    subtask_name = Test_Data_003.subtask_name
        
    def test_create_subtask(self):
        self.logger.info("*****Started Create SubTask Test******")
        
        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull ****")
        self.logger.info("****Creating Sub Task Item****")
        time.sleep(5)
        self.create_tasknotes_obj = CreateTaskNotesPage(self.driver)
        time.sleep(2)
        self.create_tasknotes_obj.click_personal_option_button()

        self.create_subtask_obj = CreateSubTaskPage(self.driver)
        
        self.create_subtask_obj.click_task_item(self.taskname)
        
        time.sleep(2)
    
        self.create_subtask_obj.scroll_task_dialog()
        
        time.sleep(3)

        self.create_subtask_obj.click_add_subtask_button()
        time.sleep(2)

        self.create_subtask_obj.enter_subtask(self.subtask_name)
        time.sleep(5)
    
        subtask = self.create_subtask_obj.subtask_item_visible()

        print(subtask)

        if self.subtask_name == subtask:
            self.logger.info("*****Create Sub Task Test passed******")
            self.move_backward()
            assert True
        else:
            self.logger.error("*****Create Sub Task Test failed******")
            self.save_screenshot("test_create_subtask.png")
            assert False