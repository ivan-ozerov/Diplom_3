
from helper import URLs
from pages.header import Header
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    def test_open_history_page(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.open_order_history()
        assert driver.current_url == URLs.ORDER_HISTORY_PAGE_URL

    def test_logout(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.logout()
        assert driver.current_url == URLs.LOGIN_PAGE_URL

    