
from pages.base_page import BasePage
from locators import Locators
from helper import URLs
from pages.header import Header
from pages.main_page import MainPage
from test_data import TestData
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.logout_button = Locators.PROFILE_PAGE_LOGOUT_BUTTON
        self.order_history_button = Locators.PROFILE_PAGE_ORDER_HISTORY_BUTTON
        self.orders_last_order_number = Locators.PROFILE_PAGE_ORDER_HISTORY_ORDERS_NUMBERS

    def open_order_history(self):
        header = Header(self.driver)
        self.wait(self.order_history_button)
        self.click(self.order_history_button)
        self.wait_page_load(URLs.ORDER_HISTORY_PAGE_URL)
        self.wait(self.orders_last_order_number)

    def logout(self):
        header = Header(self.driver)
        header.go_to_profile_page()
        self.click(self.logout_button)
        self.wait_page_load(URLs.LOGIN_PAGE_URL)

    def get_last_order_number(self):
        self.open_order_history()
        return self.get_text_of(self.orders_last_order_number)
    