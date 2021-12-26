import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options





@pytest.fixture(scope="class")
def init_driver(request):
    browser = request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield
    driver.close()
    # return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'desktop.any.do Web UI Automation'
    config._metadata['Module Name'] = 'UI Testing'
    config._metadata['Tester'] = 'Sudipta Sarker'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)