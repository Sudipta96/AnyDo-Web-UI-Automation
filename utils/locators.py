from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.ID, 'nav-logo')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')


class LoginPageLocators(object):
    # continue_with_email_btn = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]') 
    # email_input = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/input')                         
    # password_input = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input')
    # signin_btn = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/button[2]')
                            
                            #  //*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[1]/div/input
                            #    //*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[1]/div/input

    continue_with_email = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/button[3]/div/div[1]')
    email_input = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/input')
    password_input = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input')
    signin_btn = (By.XPATH, '//*[@id="root"]/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/button[2]')

    settings_icon_xpath = (By.XPATH, '//*[@id="root"]/div[2]/header/div/div/div[3]/button')
    my_profile_xpath = (By.XPATH, '/html/body/div[3]/div/div[3]/div/section/div/div/div/div/div[1]/div/div/div/button[1]/div[1]')
    sign_out_xpath = (By.XPATH, '/html/body/div[3]/div/div[3]/div/section/div/div/div/div/div[8]/div/div/div/button[3]/div[1]')

class CreateTaskLocators(object):
    create_task_button = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/div[2]/div/button/span[2]')
    enter_task_name_input = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[1]/div/div/div/textarea')
    add_task_btn = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button')
    task_list = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/section/div/article[1]/div/div[1]/article/div/div/div/div/div/div[1]')
    
    enter_notes_input =  (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[1]/div/div[2]/div[2]/div/div/textarea')
    next_week_button = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/div/div/div/div[3]/div[2]/div[2]/button[3]')

class CreateSubTaskLocators(object):
    task_item = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/section/div/article[1]/div/div[3]/article/div/div/div/div/div/div[1]/div[1]/div[1]')
                        #    '//*[@id="root"]/div[2]/div[3]/div/section/div/article[1]/div/div[3]/article/div/div/div/div/div/div[1]/div[2]/div'
                        
    subtask_btn = (By.XPATH, '/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/button/div/div[2]')
    # add_subtask_input = (By.XPATH,'/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/div/div/div[1]/input')
    subtask_item = (By.XPATH, '/html/body/div[6]/div/div/div[3]/div/div/article/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[6]/div/article/div/div/div[1]/input')
    # subtask_main = (By.CSS_SELECTOR, 'body > div.js-Portal.portal-default > div > div > div:nth-child(3) > div > div > article > div > div > div > div > div > div.TabsTab.TabsTab--active.TabsTab--fullHeight > div > div > div > div > div > div > div.TaskEditPaneDetails__subTasks.TaskEditPaneDetails__fullRow > div > article > div > div > div.SubTaskItem__mainContent')
    # add_subtask_input = (By.XPATH, '//input[@class="SubTaskItem__textField fs-hide"]')
    add_subtask_input  = (By.XPATH, '//div[@class="NewSubTaskItem"]')
                                        #    NewSubTaskItem__textField fs-hide
                                     

class CreateListLocators(object):
    add_list_icon = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[1]/div[2]/div/button[2]')
    add_list_input = (By.XPATH, '//textarea[@name="category-name"]')
                                 
    create_list_button = (By.XPATH, '/html/body/div[3]/div/div/div[3]/form/section/footer/div/div/button[2]')
    list_item = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul/li[4]')
    list_category = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul')
                                # //*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul

class AddItemToList(object):
    collapse_shortcut_icon = (By.XPATH, '//button[@class="AppSidebarCallapseButtonsBox" and @aria-label="Collapse shortcuts"]')
    listname = (By.XPATH, '//div[text()="My Shopping List"]')
                        #    //*[@id="root"]/div[2]/div[1]/div[3]/nav/ul/li[3]/div[2]/ul/li[6]/a/div[2]
    add_task_input = (By.XPATH, '//input[@class="PaneFooterTextField__input fs-hide" and @maxlength="1000"]')
    list_items_box = (By.XPATH, '//div[@class="TaskListTarget"]')

class ChangeTheme(object):
    settings_icon = (By.XPATH, '//button[@aria-label="Settings"]')
    theme_button = (By.XPATH, "//div[text()='Theme']")
    dark_theme = (By.XPATH, '//input[@name="recurrentMove" and @value="DARK"]')
    light_theme = (By.XPATH, '//input[@name="recurrentMove" and @value="LIGHT"]')


