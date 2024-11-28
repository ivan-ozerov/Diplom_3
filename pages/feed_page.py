from pages.base_page import BasePage
from locators import Locators
from helper import URLs
from test_data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 10)        #
        self.order_feed_card = Locators.FEED_PAGE__ORDER_FEED_ITEM
        self.counter_of_all_orders = Locators.FEED_PAGE__NUMBER_OF_ORDERS_ALL_TIME
        self.counter_of_orders_today = Locators.FEED_PAGE__NUMBER_OF_ORDERS_TODAY
        self.in_work_orders = Locators.FEED_PAGE__IN_WORK_SECTION_ITEMS
        self.modal_order_box = Locators.FEED_PAGE__ORDER_BOX
        self.orders_numbers = Locators.FEED_PAGE__ORDERS_NUMBERS
    
    def click_on_order_card(self):
        self.driver.get(URLs.FEED_PAGE_URL)
        self.wait(self.order_feed_card)
        self.click(self.order_feed_card)
        self.wait(self.modal_order_box)

    def user_last_order_is_displayed_in_feed_page(self, order_number):
        self.wait(self.orders_numbers)
        all_orders_numbers_elements = self.find_multiple(self.orders_numbers)
        for order_number_elemement in all_orders_numbers_elements:
            if order_number_elemement.text == order_number:
                return True 
        return False


    def get_number_of_all_orders(self):
        self.wait(self.counter_of_all_orders)
        return self.get_text_of(self.counter_of_all_orders)
    
    def get_number_of_orders_today(self):
        self.wait(self.counter_of_orders_today)
        return self.get_text_of(self.counter_of_orders_today)
    
    def get_orders_numbers_in_work(self, order_number):
        all_orders_in_work_text = []
        number = None
        for i in range(3):
            self.wait(self.in_work_orders)
            self.wait_until_value_not_present_in_element(self.in_work_orders, 'Все текущие заказы готовы!')
            self.wait_until_value_be_present_in_element(self.in_work_orders, order_number)
            number = self.find_multiple(self.in_work_orders)[0].text[1:]
            if order_number == number:
                break
        return number == order_number 
            