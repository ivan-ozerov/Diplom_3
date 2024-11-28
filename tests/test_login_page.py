
from helper import URLs
from pages.header import Header
from pages.login_page import LoginPage
import allure


class TestLoginPage:

    @allure.title('Go to main page after login')
    def test_login(self, driver, login):
        assert driver.current_url == URLs.MAIN_PAGE_URL

    @allure.title('Go to password recovery page')
    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_password_recovery_page()
        assert driver.current_url == URLs.PASSWORD_RECOVERY_PAGE_URL

    @allure.title('Go to profile page')
    def test_go_to_personal_page(self, driver, login):
        login_page = LoginPage(driver)
        header = Header(driver)
        header.go_to_profile_page()
        assert driver.current_url == URLs.PROFILE_PAGE_URL