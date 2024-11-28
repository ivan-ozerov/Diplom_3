from pages.base_page import BasePage
from locators import Locators
from helper import URLs
from test_data import TestData
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):

    driver = None
    page_url = URLs.REGISTRATION_PAGE_URL

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.email_input_field = Locators.REGISTRATION_PAGE_EMAIL_INPUT_FIELD
        self.name_input_field = Locators.REGISTRATION_PAGE_NAME_INPUT_FIELD
        self.password_input_field = Locators.REGISTRATION_PAGE_PASSWORD_INPUT_FIELD
        self.registration_button = Locators.REGISTRATION_PAGE_REGISTRATION_BUTTON

    def registration(self, credentials):
        self.driver.get(self.page_url)

        self.set_text_of(self.email_input_field, credentials['email'])
        self.set_text_of(self.name_input_field, credentials['name'])
        self.set_text_of(self.password_input_field, credentials['password'])

        self.click(self.registration_button)

        self.wait_page_load(URLs.MAIN_PAGE_URL)