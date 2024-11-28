
import time
from helper import URLs
from pages.main_page import MainPage
import allure

class TestMainPage:

    @allure.title('Open modal window after click on ingredient')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(main_page.ingredient)
        assert main_page.is_element_displayed(main_page.ingredient_card_section)

    @allure.title('Close modal window after click on close button')
    def test_close_ingredient_card(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(main_page.ingredient)
        main_page.close_ingredient_card()
        assert not main_page.is_element_displayed(main_page.ingredient_card_section)

    @allure.title('Counter increases after put ingredient in basket')
    def test_counter_increases_after_put_ingredient_in_basket(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        counter = main_page.get_counter_of_ingredient_value(main_page.ingredient_counter)
        main_page.drag_and_drop_ingredient_to_basket(main_page.ingredient)
        new_counter = main_page.get_counter_of_ingredient_value(main_page.ingredient_counter)
        assert int(new_counter) == int(counter) + 2
        
    @allure.title('Create order after click on create order button')
    def test_is_order_modal_opened_after_create_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.create_order(main_page.ingredient)
        assert main_page.is_element_displayed(main_page.order_identifiyer) and main_page.get_text_of(main_page.order_identifiyer) != '9999'