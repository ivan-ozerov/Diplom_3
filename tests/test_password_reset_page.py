from pages.password_reset_page import PasswordResetPage
from test_data import TestData
import allure



class TestPasswordResetPage:

    @allure.title('Show password button')
    def test_show_password_button(self, driver):
        password_reset_page = PasswordResetPage(driver)
        assert password_reset_page.is_password_shown(TestData.LOGIN_CORRECT_CREDENTIALS['email'])
