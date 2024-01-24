import datetime
import inspect
import logging
import time

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import Excel_Utils


@pytest.mark.usefixtures("set_up")
class BaseClass:
    path = "C:\\Users\\HP\\Documents\\Book1.xlsx"
    rows = Excel_Utils.get_rows_count(path, "Sheet1")

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def click_on_element(self, by, duration):
        element = self.wait_for_element_to_be_clickable(by, duration)
        element.click()

    def find_element(self, by):
        return self.driver.find_element(*by)

    def type_text_into_the_element(self, by, text):
        element = self.find_element(by)
        element.send_keys(text)

    def get_text_from_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return element.text
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_current_url(self):
        return self.driver.current_url

    def select_from_dropdown_visible_text(self, by, text):
        select = Select(self.driver.find_element(*by))
        select.select_by_visible_text(text)

    def select_from_dropdown_value(self, by, value):
        select = Select(self.driver.find_element(by))
        select.select_by_value(value)

    def select_from_dropdown_index(self, by, index):
        select = Select(self.driver.find_element(by))
        select.select_by_index(index)

    def wait_for_element_to_be_clickable(self, by, duration):
        wait = WebDriverWait(self.driver, duration)
        element = wait.until(EC.element_to_be_clickable(by))
        return element

    def wait_for_element_to_be_visible(self, by, duration):
        wait = WebDriverWait(self.driver, duration)
        element = wait.until(EC.visibility_of_element_located(by))
        return element

    def wait_for_element_to_be_invisible(self, by, duration):
        wait = WebDriverWait(self.driver, duration)
        element = wait.until(EC.invisibility_of_element_located(by))
        return element

    def hover_over_element(self, by):
        element = self.find_element(by)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    # by using this method : "print("Waiting for cookies to disappear...")
    # self.wait_for_element_to_be_invisible(self.cookies, 10)
    # print("Cookies have disappeared!")"
    # ------------------------------------------------------------------
    # Method for how many rows are using for testing
