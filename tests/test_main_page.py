
import time
from helper import URLs
from pages.main_page import MainPage

class TestMainPage:

    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(main_page.ingredient)
        assert main_page.is_element_displayed(main_page.ingredient_card_section)

    def test_close_ingredient_card(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(main_page.ingredient)
        main_page.close_ingredient_card()
        assert not main_page.is_element_displayed(main_page.ingredient_card_section)

    def test_counter_increases_after_put_ingredient_in_basket(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        counter = main_page.get_counter_of_ingredient_value(main_page.ingredient_counter)
        main_page.drag_and_drop_element_in_basket(main_page.ingredient)
        new_counter = main_page.get_counter_of_ingredient_value(main_page.ingredient_counter)
        assert int(new_counter) == int(counter) + 2
        
    def test_is_order_modal_opened_after_create_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.create_order(main_page.ingredient)
        # time.sleep(2)
        assert main_page.is_element_displayed(main_page.order_identifiyer) and main_page.get_text_of(main_page.order_identifiyer) != '9999'