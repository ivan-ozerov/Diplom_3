
from pages.base_page import BasePage
from locators import Locators
from helper import URLs
from test_data import TestData
from selenium.webdriver.support import expected_conditions as EC

class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.profile_page_link = Locators.HEADER_TO_PERSONAL_PAGE_LINK
        self.constructor_link = Locators.HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK
        self.main_page_link = Locators.HEADER_TO_MAIN_PAGE_APP_LOGO_LINK
        self.feed_page_link = Locators.HEADER_TO_MAIN_PAGE_FEED_LINK


    def go_to_profile_page(self):
        self.wait_element_to_be_clickable(self.profile_page_link)
        self.click(self.profile_page_link)
        self.wait_page_load(URLs.PROFILE_PAGE_URL)

    def go_to_constructor(self):
        self.go_to_profile_page()
        self.wait_element_to_be_clickable(self.constructor_link)
        self.click(self.constructor_link)
        self.wait_page_load(URLs.MAIN_PAGE_URL)

    def go_to_feed_page(self):
        self.go_to_profile_page()
        self.wait_element_to_be_clickable(self.feed_page_link)
        self.click(self.feed_page_link)
        self.wait_page_load(URLs.FEED_PAGE_URL)

    