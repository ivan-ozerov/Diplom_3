from pages.base_page import BasePage
from locators import Locators
from helper import URLs
from test_data import TestData
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    driver = None
    page_url = URLs.LOGIN_PAGE_URL

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.email_input_field = Locators.LOGIN_PAGE_EMAIL_INPUT_FIELD
        self.password_input_field = Locators.LOGIN_PAGE_PASSWORD_INPUT_FIELD
        self.login_button = Locators.LOGIN_PAGE_LOGIN_BUTTON
        self.password_recovery_page_button = Locators.LOGIN_PAGE_TO_RESTORE_PASSWORD_PAGE_LINK

    def login(self, credentials):
        self.driver.get(self.page_url)

        self.set_text_of(self.email_input_field, credentials['email'])
        self.set_text_of(self.password_input_field, credentials['password'])
        self.click(self.login_button)

        self.wait_page_load(URLs.MAIN_PAGE_URL)

    def go_to_password_recovery_page(self):
        self.driver.get(self.page_url)
        self.wait_page_load(self.page_url)

        self.click(self.password_recovery_page_button)
        self.wait_page_load(URLs.PASSWORD_RECOVERY_PAGE_URL)

        