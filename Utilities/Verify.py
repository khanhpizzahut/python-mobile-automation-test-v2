from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

class Text:

    @staticmethod
    def textview(element,driver,expected_text):
        try:
            wait = WebDriverWait(driver, 20)
            if (element[0] == "id"):
                currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, element[1])))
                text = driver.find_element_by_id(element[1]).text
            else:
                currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH, element[1])))
                text = driver.find_element_by_xpath(element[1]).text
            log.logger.info("[WATING] to verify text - showed element: " + element[1])
            assert text == expected_text
            log.logger.info("[VerifyText] as expected is: " + text)
        except():
            log.logger.info("[WATING] to verify text - error element: " + element[1])
