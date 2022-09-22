import logging

from Utilities.LogUtil import Logger
from Utilities import configReader
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def isID(self, element):
        if (element[0] == "id"):
            return True
        else:
            return False

    def waiting(self, element):
        # delay(0.5)
        try:
            wait = WebDriverWait(self.driver, 20)
            if self.isID(element):
                currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, element[1])))
            else:
                currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH, element[1])))
            log.logger.info("[WATING] showed element: " + element[1])
        except():
            log.logger.info("[WATING] error element: " + element[1])


    def click(self, element):
        self.waiting(element)
        log.logger.info("[CLICK] " + element[1])
        if self.isID(element):
            self.driver.find_element_by_id(element[1]).click()
        else:
            self.driver.find_element_by_xpath(element[1]).click()

    def input(self, element, value):
        self.waiting(element)
        log.logger.info("[INPUT] " + element[1])
        if self.isID(element):
            self.driver.find_element_by_id(element[1]).send_keys(value)
        else:
            self.driver.find_element_by_xpath(element[1]).send_keys(value)
        log.logger.info("[INPUT] with value: " + value)

    def getText(self, element):
        self.waiting(element)
        log.logger.info("[GETTEXT] " + element[1])
        if self.isID(element):
            text = self.driver.find_element_by_id(element[1]).text
        else:
            text = self.driver.find_element_by_xpath(element[1]).text
        log.logger.info("[GETTEXT] text is: " + text)
        return text

    def verifyTextview(self,element, expected_text):
        text = self.getText(element)
        log.logger.info("[VERIFY] expected is: " + expected_text)
        assert text == expected_text

    # def clickIndex(self, locator, index):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_elements_by_accessibility_id(configReader.readConfig("locators", locator))[index].click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_elements_by_id(configReader.readConfig("locators", locator))[index].click()
    #     log.logger.info("Clicking on an Element "+ str(locator) + "with index : " + str(index))
