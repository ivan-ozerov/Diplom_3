import pytest
from helper import URLs
from pages.login_page import LoginPage
from test_data import TestData
from selenium import webdriver
from pages.registration_page import RegistrationPage
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

@pytest.fixture
def firefox():
    options = Options()
    options.binary_location = '/usr/lib/firefox/firefox-bin'
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request, firefox, chrome):    
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
    