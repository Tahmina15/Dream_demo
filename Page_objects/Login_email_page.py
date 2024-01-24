import time

from selenium.webdriver.common.by import By

from Utilities.Base_utils import BaseClass


class Login(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    click_create_account = (By.CSS_SELECTOR, "a.checkout-login__register-link")

    def click_on_create_account(self):
        self.click_on_element(self.click_create_account, 10)


