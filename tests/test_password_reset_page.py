

from pages.password_reset_page import PasswordResetPage
from test_data import TestData


class TestPasswordResetPage:

    def test_show_password_button(self, driver):
        password_reset_page = PasswordResetPage(driver)
        password_in_input_field = password_reset_page.show_password(driver, 
                                                                    TestData.LOGIN_CORRECT_CREDENTIALS['email'])
        assert password_in_input_field == 'text'
