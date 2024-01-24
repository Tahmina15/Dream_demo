import pytest

from Page_objects.Cart_page import Cart
from Page_objects.Home_page import HomePage
from Page_objects.Login_email_page import Login
from Page_objects.Login_register_page import Login_register
from Page_objects.Lucia_wilson_collection_page import Lucia_wilson_collection_Page
from Utilities.Base_utils import BaseClass


class TestOne(BaseClass):

    def test_user_should_register_successfully(self):
        homepage = HomePage(self.driver)
        login = Login(self.driver)
        login_register = Login_register(self.driver)
        homepage.cookies_handler()
        homepage.my_account()
        login.click_on_create_account()
        login_register.register_credentials()

    def test_end2end(self):
        homepage = HomePage(self.driver)
        lucia_wilson_collection_page = Lucia_wilson_collection_Page(self.driver)
        cart_page = Cart(self.driver)
        #homepage.cookies_handler()
        homepage.search_items()
        homepage.search_button()
        lucia_wilson_collection_page.verify_the_page()
        cart_page.save_the_item()
