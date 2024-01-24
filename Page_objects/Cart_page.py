from selenium.webdriver.common.by import By

from Utilities.Base_utils import BaseClass


class Cart(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    save_item = (By.CSS_SELECTOR, "a.js-saveShortlistCart.cart-new-checkout__shortlist--link")
    my_shortlist = (By.CSS_SELECTOR, "a.mini-shortlist__link")
    view_short_list = (By.XPATH, "//a[normalize-space()='View my shortlist']")

    # method to generate save the item for later
    def save_the_item(self):
        self.click_on_element(self.save_item, 5)

    def hover_on_shortlist(self):
        self.hover_over_element(self.my_shortlist)
        self.click_on_element(self.view_short_list, 20)

