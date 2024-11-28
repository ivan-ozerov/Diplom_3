
from helper import URLs
from pages.feed_page import FeedPage
from pages.header import Header
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import allure

class TestHeader:

    @allure.title('Go to profile page')
    def test_go_to_profile_page(self, driver, login):
        header = Header(driver)
        header.go_to_profile_page()
        ProfilePage(driver).wait(ProfilePage(driver).logout_button)
        assert driver.current_url == URLs.PROFILE_PAGE_URL

    @allure.title('Go to constructor page')
    def test_go_to_constructor(self, driver, login):
        header = Header(driver)
        header.go_to_constructor()
        MainPage(driver).wait(MainPage(driver).create_order_button)
        assert driver.current_url == URLs.MAIN_PAGE_URL and 'active' in header.get_attribute_of(header.constructor_link, 'class')

    @allure.title('Go to feed page')
    def test_go_to_feed_page(self, driver, login):
        header = Header(driver)
        header.go_to_feed_page()
        FeedPage(driver).wait(FeedPage(driver).orders_numbers)
        assert driver.current_url == URLs.FEED_PAGE_URL and 'active' in header.get_attribute_of(header.feed_page_link, 'class')

    