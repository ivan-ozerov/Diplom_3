
from helper import URLs
from pages.login_page import LoginPage


class TestLoginPage:

    def test_login(self, driver, login):
        assert driver.current_url == URLs.MAIN_PAGE_URL

    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_password_recovery_page()
        assert driver.current_url == URLs.PASSWORD_RECOVERY_PAGE_URL

    