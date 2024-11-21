import pytest
from helper import URLs
from pages.login_page import LoginPage
from test_data import TestData
from selenium import webdriver
from pages.registration_page import RegistrationPage

@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture
def firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request, chrome, firefox):    
    if request.param == 'chrome':
        yield chrome
        chrome.quit()
    else:
        yield firefox
        firefox.quit()
    

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
    