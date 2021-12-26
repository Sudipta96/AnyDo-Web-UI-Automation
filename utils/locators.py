from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    continue_with_email = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]/div/div[1]')
    email_input = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/input')
    password_input = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input')
    signin_btn = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/button[2]')


class CreateTaskLocators(object):
    create_task_button = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/div[2]/div/button/span[2]')
    enter_task_name_input = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[1]/div/div/div/textarea')
    add_task_btn = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button')
    task_list = (By.XPATH, '//div[@class="TaskListTarget"]')
    

class CreateTaskNotesLocators(object):
    enter_notes_input =  (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[2]/div[2]/div/div/textarea')
    next_week_button = (By.XPATH, '//button[text()="Next week"]')
    personal_option_button = (By.XPATH, '//div[text()="Personal"]')
    


class CreateSubTaskLocators(object):
    task_dialog = (By.XPATH, '//div[@class="TaskEditPaneDetails"]')
    next_seven_days_button = (By.XPATH, '//a[@href="/tasks/next-seven-days"]')
    task_item = (By.XPATH, '//div[@class="TaskItem__title__text fs-hide" and text()="My Friday Task"]')
    task_list = (By.XPATH, '//div[@class="TaskListTarget"]')
    
    add_subtask_btn = (By.XPATH, '//div[text()="Add a new subtask"]')
    add_subtask_input  = (By.XPATH, '//div[@class="NewSubTaskItem"]')
    subtask_item = (By.XPATH, '//input[@class="SubTaskItem__textField fs-hide"]')
    

class CreateListLocators(object):
    add_list_icon = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[1]/div[2]/div/button[2]')
    add_list_input = (By.XPATH, '//textarea[@name="category-name"]')
                                 
    create_list_button = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button[2]')
    list_item = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul/li[4]')
    list_category = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul')
                            

class AddItemToList(object):
    collapse_shortcut_icon = (By.XPATH, '//button[@class="AppSidebarCallapseButtonsBox" and @aria-label="Collapse shortcuts"]')
    listname = (By.XPATH, '//div[text()="My Shopping List"]')
                      
    add_task_input = (By.XPATH, '//input[@class="PaneFooterTextField__input fs-hide" and @maxlength="1000"]')
    list_items_box = (By.XPATH, '//div[@class="TaskListTarget"]')

class ChangeTheme(object):
    settings_icon = (By.XPATH, '//button[@aria-label="Settings"]')
    theme_button = (By.XPATH, "//div[text()='Theme']")
    dark_theme = (By.XPATH, '//input[@name="recurrentMove" and @value="DARK"]')
    light_theme = (By.XPATH, '//input[@name="recurrentMove" and @value="LIGHT"]')


class CheckNotification(object):
    notification_button = (By.XPATH, '//button[@title="Notifications"]')
    notification_menu = (By.XPATH, '//div[@class="NotificationsMenu"]')
    notification_updates_button = (By.XPATH, '//button//span[text()= "Updates"]')

class AddSelectionFeature(object):
    collapse_shortcut_button = (By.XPATH, '//button[@class="AppSidebarCallapseButtonsBox" and @aria-label="Collapse shortcuts"]')
    list_item = (By.XPATH, '//div[text()="My Shopping List"]')
    more_options_icon = (By.XPATH, '//button[@aria-label="More options"]')
    mutiple_selection_button = (By.XPATH, '//button[@class="TasksToolBarSettings__item__button" and text()="Multiple selection (B)"]')
    taskbatchtoolbar = (By.XPATH, '//div[@class="TaskBatchToolbar"]')
    task_selected_items_count = (By.XPATH, '//div[@class="TaskBatchToolbar__badge__text"]')
    task_list_container = (By.XPATH, '//div[@class="TaskListTarget"]')

class Createtag(object):
    collapse_shortcuts = (By.XPATH, '//button[@aria-label="Collapse shortcuts"]')
    collapse_list_shortcuts = (By.XPATH, '//button[@aria-label="Collapse lists"]')
    add_tag_icon = (By.XPATH, '//div[@class="AppSidebarHeadingItem__utils"]/button[2][@class="AppSidebarLabels__button"]')
    no_thanks_button = (By.XPATH, '//button[@class="PremiumPage2__dismissButton"]')
    collapse_list = (By.XPATH, '[class="AppSidebarCallapseButtonsBox"]')

class LogoutLocators(object):
    settings_icon = (By.XPATH, '//*[@id="root"]/div[2]/header/div/div/div[3]/button')
    my_profile_button = (By.XPATH, '/html/body/div[3]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[1]/div[1]')
    sign_out_button= (By.XPATH, '/html/body/div[3]/div/div[3]/div/section/div/div/div/div/div[8]/div/div/div/button[3]/div[1]')