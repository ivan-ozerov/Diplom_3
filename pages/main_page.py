
from pages.base_page import BasePage
from locators import Locators
from helper import URLs, Driver
from test_data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.ingredient = Locators.MAIN_PAGE_CONSTRUCTOR_BUN_ELEMENT
        self.ingredient_card_section = Locators.MAIN_PAGE_CONSTRUCTOR_INGREDIENT_CARD_SECTION
        self.ingredient_card_info = Locators.MAIN_PAGE_CONSTRUCTOR_INGREDIENT_CARD_INFO
        self.ingredient_card_close_button  = Locators.MAIN_PAGE_CONSTRUCTOR_INGREDIENT_CARD_CLOSE_BUTTON
        self.ingredient_counter = Locators.MAIN_PAGE_CONSTRUCTOR_IGREDIENT_COUNTER
        self.constructor_basket = Locators.MAIN_PAGE_CONSTRUCTOR_BUSKET
        self.create_order_button = Locators.MAIN_PAGE_CONSTRUCTOR_ORDER_BUTTON
        self.order_identifiyer = Locators.MAIN_PAGE_CONSTRUCTOR_ORDER_IDENTIFIER
        self.order_modal_close_button = Locators.MAIN_PAGE_ORDER_CLOSE_BUTTON
        
    def go_to_main_page(self):
        self.driver.get(URLs.MAIN_PAGE_URL)
        self.wait_page_load(URLs.MAIN_PAGE_URL)


    def click_on_ingredient(self, element_locator):
        self.wait(element_locator)
        self.click(element_locator)
        self.wait(self.ingredient_card_section)

    def close_ingredient_card(self):
        # self.click_on_ingredient(element_locator)
        self.wait_element_to_be_clickable(self.ingredient_card_close_button)
        self.click(self.ingredient_card_close_button)
        print(self.is_element_displayed(self.ingredient_card_close_button))
        self.wait_unt_not(self.ingredient_card_section)

    def get_counter_of_ingredient_value(self, element_locator):
        counter = self.get_text_of(element_locator)
        return counter
    
    def drag_and_drop_ingredient_to_basket(self, element_locator_to_drag):
        return self.drag_and_drop_element(element_locator_to_drag, self.constructor_basket)    

    def click_create_order_button(self):
        self.click(self.create_order_button)
        self.wait(self.order_identifiyer)
        return self.order_identifiyer


    def create_order(self, element_locator):
        self.go_to_main_page()
        self.wait(element_locator)
        self.drag_and_drop_ingredient_to_basket(element_locator)
        self.click_create_order_button()
        self.wait_until_value_not_present_in_element(self.order_identifiyer, '9999')

    
    def close_order_modal(self):
        self.wait(self.order_modal_close_button)
        self.wait_element_to_be_clickable(self.order_modal_close_button)
        self.click(self.order_modal_close_button)