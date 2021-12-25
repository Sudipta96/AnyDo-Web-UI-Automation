import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.create_tasknotes_page import CreateTaskNotesPage
from tests.base_test import BaseTest
from utils.readProperties import ReadConfig
from utils.customLogger import LogGeneration
from configurations.config import TestData, Test_Data_002
import time 



class Test_002_Create_TaskNotes(BaseTest):
    username = TestData.username
    password = TestData.password
    logger= LogGeneration.loggen()

    taskname = Test_Data_002.taskname
    notes_name = Test_Data_002.notes_name
        
    def test_create_task_with_notes_and_reminder(self):
        self.logger.info("*****Started Create Task Test******")
        
        self.logger.info("****Login process initializing ****")
        self.lp=LoginPage(self.driver)
        
        self.lp.login(self.username, self.password)
        self.logger.info("****Login successfull ****")

        self.logger.info("****Started creating task ****")
        self.create_task_obj = CreateTaskNotesPage(self.driver)
        self.create_task_obj.click_create_task_btn()
        self.create_task_obj.enter_task_name(self.taskname)

        self.create_task_obj.enter_notes_name(self.notes_name)
        time.sleep(2)
        self.create_task_obj.click_next_week_button()
        time.sleep(2)
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