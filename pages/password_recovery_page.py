

from helper import URLs
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    page_url = URLs.PASSWORD_RECOVERY_PAGE_URL
    driver = None

    def __init__(self, driver):
        super().__init__(driver, 10)    
        
    # def go_to_password_restore_page(self):
    