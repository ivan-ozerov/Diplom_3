import time
from helper import URLs
from pages.feed_page import FeedPage
from pages.header import Header
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import allure


class TestFeedPage:

    @allure.title('Open order modal after click on order card')
    def test_open_order_modal_after_click_on_order_card(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_order_card()
        assert feed_page.is_element_displayed(feed_page.modal_order_box)

    @allure.title('User orders are displayed in feed page')
    def test_user_orders_are_displayed_in_feed_page(self, driver, login):
        main_page = MainPage(driver)
        main_page.create_order(main_page.ingredient)
        main_page.close_order_modal()
        profile_page = ProfilePage(driver)
        header = Header(driver)
        header.go_to_profile_page()
        profile_page.open_order_history()
        profile_page.wait(profile_page.orders_last_order_number)
        print(driver.current_url)
        last_order_number = profile_page.get_last_order_number()
        driver.get(URLs.FEED_PAGE_URL)
        feed_page = FeedPage(driver)
        assert feed_page.user_last_order_is_displayed_in_feed_page(last_order_number)
        
    @allure.title('Counter of all orders is increased after create order')
    def test_counter_of_all_orders_is_increased_after_create_order(self, driver, login):
        driver.get(URLs.FEED_PAGE_URL)
        feed_page = FeedPage(driver)
        number_of_all_orders_before = feed_page.get_number_of_all_orders()
        number_of_orders_today_before = feed_page.get_number_of_orders_today()
        main_page = MainPage(driver)
        main_page.create_order(main_page.ingredient)
        driver.get(URLs.FEED_PAGE_URL)
        assert feed_page.get_number_of_all_orders() > number_of_all_orders_before and feed_page.get_number_of_orders_today() > number_of_orders_today_before


    @allure.title('Is order in block in work')
    def test_is_order_in_block_in_work(self, driver, login):
        main_page = MainPage(driver)
        main_page.create_order(main_page.ingredient)
        main_page.wait_until_value_not_present_in_element(main_page.order_identifiyer, '9999')
        order_number = main_page.get_text_of(main_page.order_identifiyer)
        driver.get(URLs.FEED_PAGE_URL)
        feed_page = FeedPage(driver)
        assert feed_page.get_orders_numbers_in_work(order_number)

        