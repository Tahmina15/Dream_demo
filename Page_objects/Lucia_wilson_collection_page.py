import time

from selenium.webdriver.common.by import By

from Utilities.Base_utils import BaseClass


class Lucia_wilson_collection_Page(BaseClass):

    def __init__(self, driver):
        self.driver = driver
# wilson upholstered ottoman Bed frame= '//div[@class="product-tile"]/div[@class="product-tile__details"]//h2//a[@href="/wilson-upholstered-ottoman-bed-frame/p/251-00149"]')
    # Title locator
    title_locator = (By.CSS_SELECTOR, "h1.dreams-product-lister__title")
    # for dynamically use the locator need to just change the title
    lucia_bed = (By.XPATH, '//div[@class="product-tile"]/div[@class="product-tile__details"]//h2//a[@href="/lucia-upholstered-bed-frame/p/251-00268"]')
    add_to_basket = (By.CSS_SELECTOR, "button.ajax-button.dreams-button")
    continue_button = (
        By.CSS_SELECTOR, "a.dreams-button.dreams-button--pink-light.dreams-pdp-interstitial__bottom-continue-to-basket")

    def verify_the_page(self):
        print("Page URL : " + self.driver.current_url)
        actual_title = self.driver.find_element(*self.title_locator).text
        print("Page Title: " + actual_title)

        expected_title = "Lucia / Wilson Collection|"
        assert actual_title, expected_title
        self.click_on_element(self.lucia_bed, 20)
        self.click_on_element(self.add_to_basket, 10)
        self.click_on_element(self.continue_button, 10)
