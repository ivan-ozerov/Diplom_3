from selenium import webdriver


class URLs:
    # main page
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
    # login page
    LOGIN_PAGE_URL = MAIN_PAGE_URL + 'login'
    # profile page
    PROFILE_PAGE_URL = MAIN_PAGE_URL + 'account/profile'
    # registration page
    REGISTRATION_PAGE_URL = MAIN_PAGE_URL + 'register'
    # password recovery page
    PASSWORD_RECOVERY_PAGE_URL = MAIN_PAGE_URL + 'forgot-password'  
    # reset password page
    RESET_PASSWORD_PAGE_URL = MAIN_PAGE_URL + 'reset-password'
    # feed page
    FEED_PAGE_URL = MAIN_PAGE_URL + 'feed'
    # history page
    ORDER_HISTORY_PAGE_URL = MAIN_PAGE_URL + 'account/order-history'
    
    
class Driver:
    
    counter = 0
    drivers = ['chrome', 'firefox']
    current_driver = None
    
    @classmethod
    def return_driver(cls):
        cls.current_driver = cls.drivers[cls.counter]
        cls.counter = (cls.counter+1) % len(cls.drivers)
        if cls.current_driver == 'chrome':
            return webdriver.Chrome()
        elif cls.current_driver == 'firefox':
            return webdriver.Firefox()