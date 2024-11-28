from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from helper import Driver


class BasePage:

    def __init__(self, driver, waiting_time):
        self.driver = driver
        self.waiting_time = waiting_time

    def find(self, element_locator):
        return self.driver.find_element(*element_locator)

    def find_multiple(self,element_locator):
        return self.driver.find_elements(*element_locator)

    def wait(self, element_locator):
        return WebDriverWait(self.driver, self.waiting_time).until(EC.visibility_of_element_located(element_locator))

    def wait_unt_not(self, element_locator):
        return WebDriverWait(self.driver, self.waiting_time).until_not(EC.visibility_of_element_located(element_locator))

    def wait_page_load(self, url_to_be):
        return WebDriverWait(self.driver, self.waiting_time).until(EC.url_to_be(url_to_be))

    def click(self, element_locator):
        self.driver.execute_script("arguments[0].click();", self.find(element_locator))
        # self.driver.execute_script("arguments[0].click();", element_locator)
    
    def get_text_of(self, element_locator):
        return self.find(element_locator).text
    
    def get_text_of_element(self, element):
        return element.text

    def set_text_of(self, element_locator, text):
        self.find(element_locator).send_keys(text)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def unfocus(self, element_locator):
        self.find(element_locator).send_keys(Keys.TAB)

    def get_attribute_of(self, element_locator, attribute):
        return self.find(element_locator).get_dom_attribute(attribute)
    
    def is_element_displayed(self, element_locator):
        return self.find(element_locator).is_displayed()
    
    def wait_until_value_not_present_in_element(self, element_locator, value):
        WebDriverWait(self.driver, self.waiting_time).until_not(EC.text_to_be_present_in_element(element_locator, value))
        
    def wait_until_value_be_present_in_element(self, element_locator, value):
        WebDriverWait(self.driver, self.waiting_time).until(EC.text_to_be_present_in_element(element_locator, value))

    def wait_element_to_be_clickable(self, element_locator):
        return WebDriverWait(self.driver, self.waiting_time).until(EC.element_to_be_clickable(element_locator))

    def drag_and_drop_element(self, element_locator_to_drag, element_locator_to_drop):
        element_to_drag = self.find(element_locator_to_drag)
        element_to_drop = self.find(element_locator_to_drop)
        if Driver.current_driver == 'chrome':
            ActionChains(self.driver).drag_and_drop(self.find(element_locator_to_drag), self.find(element_locator_to_drop)).perform()
        elif Driver.current_driver == 'firefox':
            self.wait(element_locator_to_drag)
            self.wait(element_locator_to_drop)
            actions = ActionChains(self.driver)
            actions.move_to_element(element_to_drag).click(element_to_drag).perform()
            self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_to_drag, element_to_drop)
