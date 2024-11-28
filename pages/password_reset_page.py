
from helper import URLs
from locators import Locators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from test_data import TestData


class PasswordResetPage(BasePage):
    page_url = URLs.RESET_PASSWORD_PAGE_URL
    driver = None

    def __init__(self, driver):
        super().__init__(driver, 5)
        self.password_field = Locators.PASSWORD_RESET_PAGE_PASSWORD_INPUT_FIELD
        self.password_show_button = Locators.PASSWORD_RESET_PAGE_SHOW_PASSWORD_BUTTON

    def go_to_this_page(self, email):
        password_recovery_page = PasswordRecoveryPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.go_to_password_recovery_page()
        password_recovery_page.go_to_password_reset_page(email)
        

    def is_password_shown(self, email):
        self.go_to_this_page(email)
        self.wait(self.password_show_button)
        self.wait_element_to_be_clickable(self.password_show_button)
        self.click(self.password_show_button)
        return self.get_attribute_of(self.password_field, 'type') == 'text'

