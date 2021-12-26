from pages.login_page import LoginPage
from pages.create_tasknotes_page import CreateTaskNotesPage
from pages.create_task_page import CreateTaskPage
from tests.base_test import BaseTest
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
        self.create_task_obj = CreateTaskPage(self.driver)
        self.create_task_obj.click_create_task_btn()
        self.create_task_obj.enter_task_name(self.taskname)

        self.create_note_obj = CreateTaskNotesPage(self.driver)
        
        self.create_note_obj.enter_notes_name(self.notes_name)
        time.sleep(2)
        self.create_note_obj.click_next_week_button()
        time.sleep(2)
        self.create_task_obj.click_add_task_btn()
        time.sleep(5)

        self.create_note_obj.click_personal_option_button()

        assert self.create_task_obj.is_task_added(self.taskname)
       