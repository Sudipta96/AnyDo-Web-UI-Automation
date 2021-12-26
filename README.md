# AnyDo Web UI Automation with Selenium and Pytest

website link: https://desktop.any.do/

# Feature
1. Unit Testing with pytest
2. Browser Automation with Selenium
3. Generate html report
4. You can run tests parallelly.
5. Choose browser for test using command line arguement.
6. Gererate Log for every test. 

This project has 10 test cases along with login test case. 


# Warning

1. Some test may fail due to browser unusual interaction within specified time.
2. Login test is executed to run every test. Repeatative login on this site within few moments, this site 
   may restrict user to login and redirect to create account page.
3. Before running all the test 2nd time, please delete items(Tasks, Notes) in website at first time.



Step 1: 

i. To run this script, path of browser(chrome, firefox) webdriver should be added in system environment variables path. 

ii. You need to activate the virtual environment before running test:

Go to 'AnyDo Web UI Automation' directory

```
> cd venv\scripts
> activate

```

Step 2: To run a single test:

```
> pytest -s -v tests\test_001_create_task.py

```

By default it will use Chrome Browser for Automation.

Step 3: To choose suitable browser, You can use command line arguement. For this, 
        you need to specify browser name('firefox', 'chrome') after --browser keyword.

```
> pytest -s -v tests\test_001_create_task.py --browser chrome

or 

> pytest -s -v tests\test_001_create_task.py --browser firefox
```

Step 4: To generate report:

```
> pytest -s -v --html=Reports\report.html tests\test_001_create_task.py --browser chrome

```
Step 5: Check log file in 'Logs' folder. It's name is automation.log

Step 6: If log is not captured in report.html. Try:

```
> pytest -s -v --capture=tee-sys --html=Reports\report.html tests\test_001_create_task.py --browser chrome

```
Step 7: To run all test at a same time:

```
> pytest -s -v --capture=tee-sys --html=Reports\report.html tests --browser chrome

```

Step 8: To run all test parallelly specify number after '-n' arguement. Less number is recommended 
because large number will slow down the execution process.

```
> pytest -s -v -n 2 --capture=tee-sys --html=Reports\report.html tests --browser firefox

```




