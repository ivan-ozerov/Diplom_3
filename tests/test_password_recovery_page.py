
from helper import URLs
from pages.password_recovery_page import PasswordRecoveryPage
from test_data import TestData
import allure


class TestPasswordRecoveryPage:

    @allure.title('Go to password restore page')
    def test_go_to_password_restore_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.go_to_password_reset_page(TestData.LOGIN_CORRECT_CREDENTIALS['email'])
        assert driver.current_url == URLs.RESET_PASSWORD_PAGE_URL