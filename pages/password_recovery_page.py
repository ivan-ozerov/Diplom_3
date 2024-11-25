
from helper import URLs
from locators import Locators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from test_data import TestData


class PasswordRecoveryPage(BasePage):

    page_url = URLs.PASSWORD_RECOVERY_PAGE_URL
    driver = None

    def __init__(self, driver):
        super().__init__(driver, 10)    
        self.email_field = Locators.PASSWORD_RECOVERY_PAGE_EMAIL_FIELD
        self.recovery_button = Locators.PASSWORD_RECOVERY_PAGE_RECOVERY_BUTTON
        
    def go_to_password_reset_page(self, driver, email):
        login_page = LoginPage(driver)
        login_page.go_to_password_recovery_page()
        self.wait_page_load(self.page_url)
        self.set_text_of(self.email_field, email)
        self.click(self.recovery_button)
        self.wait_page_load(URLs.RESET_PASSWORD_PAGE_URL)