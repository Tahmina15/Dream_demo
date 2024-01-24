import time
from selenium.webdriver.common.by import By
from Utilities.Base_utils import BaseClass


class HomePage(BaseClass):
    # constractor which accept driver as an argument
    def __init__(self, driver):
        self.driver = driver

    cookies = (By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
    search = (By.XPATH, "//INPUT[contains(@class,'search__field')]")
    item = (By.XPATH, "//BUTTON[normalize-space(.)='Search']")
    my_account_click = (By.XPATH, '//a[@href="/login/email"]')

    def my_account(self):
        self.click_on_element(self.my_account_click, 2)

    def cookies_handler(self):
        log = self.get_logger()
        log.info("Page title : " + self.driver.title)
        log.info("Page URL : " + self.driver.current_url)
        self.wait_for_element_to_be_visible(self.cookies, 10)
        self.click_on_element(self.cookies, 20)

    def search_items(self):
        self.type_text_into_the_element(self.search, "Lucia")

    def search_button(self):
        self.click_on_element(self.item, 10)
