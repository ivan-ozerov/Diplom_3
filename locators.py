 # type: ignore
from selenium import webdriver
from selenium.webdriver.common.by import By

class Locators:

    #header

    # лого сайта
    HEADER_TO_MAIN_PAGE_APP_LOGO_LINK = (By.XPATH, "//header//div[contains(@class, 'header__logo')]//a[@href='/']")
    # кнопка "Личный кабинет"
    HEADER_TO_PERSONAL_PAGE_LINK = (By.XPATH, "//header//a[@href='/account']")
    # кнопка "Конструктор"
    HEADER_TO_MAIN_PAGE_CONSTRUCTOR_LINK = (By.XPATH, "//header//p[text()='Конструктор']/parent::a[@href='/']")
    # кнопка "Конструктор" в активном состоянии  
    HEADER_TO_MAIN_PAGE_CONSTRUCTOR_ACTIVE_STATE_LINK = (By.XPATH, "//header//p[text()='Конструктор']/parent::a[contains(@class,'link_active')]")
    # кнопка "Лента заказов"
    HEADER_TO_MAIN_PAGE_FEED_LINK = (By.XPATH, "//header//p[text()='Лента Заказов']/parent::a[@href='/feed']")


    #registration page

    # инпут "Имя" на странице регистрации
    REGISTRATION_PAGE_NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    # инпут "email" на странице регистрации
    REGISTRATION_PAGE_EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/parent::div/input")
    # инпут "Пароль" на странице регистрации
    REGISTRATION_PAGE_PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div/input")
    # кнопка "Зарегистрироваться" 
    REGISTRATION_PAGE_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # кнопка "Войти" на странице регистрации
    REGISTRATION_PAGE_TO_LOGIN_PAGE_LINK = (By.XPATH, "//a[text()='Войти' and @href='/login']")
    # ошибка при вводе пароля <6 символов
    REGISTRATION_PAGE_INCORRECT_PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error') and text()='Некорректный пароль']")

    #login page

    # инпут "Имя" на странице входа
    LOGIN_PAGE_NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    # инпут "email" на странице входа
    LOGIN_PAGE_EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/parent::div/input")
    # инпут "Пароль" на странице входа
    LOGIN_PAGE_PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div/input")
    # кнопка "Войти" на странице входа
    LOGIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # кнопка "Зарегистрироваться" на странице входа
    LOGIN_PAGE_TO_REGISTRATION_PAGE_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # кнопка "Восстановить пароль" на странице входа
    LOGIN_PAGE_TO_RESTORE_PASSWORD_PAGE_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    

    #main page

    # кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_TO_LOGIN_PAGE_LINK = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # кнопка "Булки" на главной странице
    MAIN_PAGE_CONSTRUCTOR_BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::div")
    # кнопка "Соусы" на главной странице
    MAIN_PAGE_CONSTRUCTOR_SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::div")
    # кнопка "Начинки" на главной странице
    MAIN_PAGE_CONSTRUCTOR_FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::div")
    # элемент "Флюоресцентная булка R2-D3" в списке "Булки"
    MAIN_PAGE_CONSTRUCTOR_BUN_ELEMENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    # элемент "Соус традиционный галактический" в списке "Соусы"
    MAIN_PAGE_CONSTRUCTOR_SAUCE_ELEMENT = (By.XPATH, "//p[text()='Соус традиционный галактический']/parent::a")
    # элемент "Мясо бессмертных моллюсков Protostomia" в списке "Начинки"
    MAIN_PAGE_CONSTRUCTOR_FILLING_ELEMENT = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']/parent::a")
    # секция с карточкой ингредиента
    MAIN_PAGE_CONSTRUCTOR_INGREDIENT_CARD_SECTION = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    # карточка ингредиента с описанием ингредиента
    MAIN_PAGE_CONSTRUCTOR_INGREDIENT_CARD_INFO = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    # кнопка "Закрыть" в карточке ингредиента
    MAIN_PAGE_CONSTRUCTOR_INGREDIENT_CARD_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    # счетчик количества ингредиента в заказе
    MAIN_PAGE_CONSTRUCTOR_IGREDIENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a//p[contains(@class, 'num')]")
    # кнопка "Оформить заказ"
    MAIN_PAGE_CONSTRUCTOR_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # корзина
    MAIN_PAGE_CONSTRUCTOR_BUSKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    # модалка с идентификатором заказа
    MAIN_PAGE_CONSTRUCTOR_ORDER_IDENTIFIER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2[contains(@class, 'Modal_modal__title')]")
    # кнопка "Закрыть" в модалке с заказом
    MAIN_PAGE_ORDER_CLOSE_BUTTON = (By.XPATH, "//p[text()='идентификатор заказа']/parent::div/following-sibling::button[contains(@class, 'Modal_modal__close')]")


    #profile page
 
    # кнопка "Выход" в Личном кабинете
    PROFILE_PAGE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # кнопка "История заказов" в Личном кабинете
    PROFILE_PAGE_ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']") 
    # заказы пользователя в Истории заказов
    PROFILE_PAGE_ORDER_HISTORY_ORDERS_NUMBERS = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits')])[last()]")

    #password_recovery_page    

    # кнопка "Войти" на странице восстановления пароля
    PASSWORD_RECOVERY_PAGE_TO_LOGIN_PAGE_LINK = (By.XPATH, "//a[text()='Войти' and @href='/login']")
    # поле ввода email
    PASSWORD_RECOVERY_PAGE_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
    # кнопка "Восстановить"
    PASSWORD_RECOVERY_PAGE_RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  

    #password_reset_page

    # кнопка "показать пароль"
    PASSWORD_RESET_PAGE_SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".input__icon.input__icon-action svg")
    # поле ввода нового пароля
    PASSWORD_RESET_PAGE_PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    # поле 

    #feed page

    # карточка заказа в ленте заказов
    FEED_PAGE__ORDER_FEED_ITEM = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    # номер заказа
    FEED_PAGE__ORDERS_NUMBERS = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//p[contains(@class, 'text_type_digits')]")
    # счетчик заказов за все время
    FEED_PAGE__NUMBER_OF_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    # счетчик заказов за все время
    FEED_PAGE__NUMBER_OF_ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    # блок "В работе"
    FEED_PAGE__IN_WORK_SECTION_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li")
    # блок с подробностями о заказе
    FEED_PAGE__ORDER_BOX = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
