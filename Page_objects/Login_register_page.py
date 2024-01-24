import time

from selenium.webdriver.common.by import By

from Utilities import Excel_Utils
from Utilities.Base_utils import BaseClass

path = "C:\\Users\\HP\\Documents\\Book1.xlsx"
rows = Excel_Utils.get_rows_count(path, "Sheet1")


class Login_register(BaseClass):

    # constractor which accept driver as an argument
    def __init__(self, driver):
        self.driver = driver

    title = (By.NAME, "titleCode")
    first_name = (By.XPATH, "//input[@id='register.firstName']")
    last_name = (By.XPATH, "//input[@id='register.lastName']")
    email = (By.XPATH, "//input[@class='form-control js-formField register-form__input js-registerEmail is-required']")
    confirm_email = (By.XPATH, "//input[@id='register.chkEmail']")
    password = (By.XPATH, "//input[@id='password']")
    confirm_pw = (By.XPATH, "//input[@id='register.checkPwd']")
    captcha = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")

    def register_credentials(self):
        log = self.get_logger()
        for i in range(2, rows + 1):
            status_title = Excel_Utils.read_data(path, "Sheet1", i, 1)
            firstName = Excel_Utils.read_data(path, "Sheet1", i, 2)
            lastName = Excel_Utils.read_data(path, "Sheet1", i, 3)
            email_address = Excel_Utils.read_data(path, "Sheet1", i, 4)
            pass_word = Excel_Utils.read_data(path, "Sheet1", i, 5)
            log.info("Page URL : " + self.driver.current_url)
            log.info(f"row:{i},FirstName:{firstName},LastName{lastName},Emai:{email_address},Password:{pass_word}")
            self.select_from_dropdown_visible_text(self.title, status_title)
            self.type_text_into_the_element(self.first_name, firstName)
            self.type_text_into_the_element(self.last_name, lastName)
            self.type_text_into_the_element(self.email, email_address)
            self.type_text_into_the_element(self.confirm_email, email_address)
            self.type_text_into_the_element(self.password, pass_word)
            self.type_text_into_the_element(self.confirm_pw, pass_word)

            # self.driver.find_element(*Login_register.captcha).click()
            # page_title = self.driver.title
            # if page_title == "register successfully":
            #     print("Register successful")
            # else:
            #     print("Register is not successful")
