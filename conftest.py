import pytest
from helper import URLs, Driver
from pages.login_page import LoginPage
from test_data import TestData
from selenium import webdriver
from pages.registration_page import RegistrationPage

@pytest.fixture(params=range(len(Driver.drivers)))
def driver():
    driver = Driver.return_driver()
    yield driver
    driver.quit()
    
@pytest.fixture
def registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.registration(TestData.REGISTTRATION_CORRECT_CREDENTIALS)
    registration_page.wait_page_load(URLs.MAIN_PAGE_URL)


@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.login(TestData.LOGIN_CORRECT_CREDENTIALS)
    login_page.wait_page_load(URLs.MAIN_PAGE_URL)
    