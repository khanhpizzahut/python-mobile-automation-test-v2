import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


#@pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def appium_driver(request):
    log.logger.info("[DRIVER] --> Start")
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['appPackage'] = 'com.phdv.universal'
    desired_caps['appActivity'] = 'com.phdv.universal.feature.main.MainActivity'
    #desired_caps['appPackage'] = 'com.goibibo'
    #desired_caps['appActivity'] = '.common.HomeActivity'
    desired_caps['noReset'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    log.logger.info("[DRIVER] --> Quit")
    driver.quit()

@pytest.fixture()
def backtohome(request, appium_driver):
    yield
    item = request.node
    tc_name = request.node.name
    #print("tc_name: " + tc_name)
    #driver = appium_driver

    if item.rep_call.failed:
        pass
        #print("failed cmnr -backtohome")
    else:
        pass
        #print("pass nha may")

