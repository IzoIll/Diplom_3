from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[(text() = 'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[(text() = 'Лента Заказов')]")
    POPUP_WINDOW = [By.XPATH, "//h2 [@class = 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10' and text() = 'Детали ингредиента']"]
    CLOSE_POPUP_BUTTON =  [By.XPATH, "//div [@class = 'Modal_modal__container__Wo2l_']/ button"]
    INGREDIENT = [By.XPATH, "//a [@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']"]
    CONSTRUCTOR_DROP = [By.XPATH, "// section [@class = 'BurgerIngredients_ingredients__1N8v2']"]
    INGREDIENT_COUNTER = [By.XPATH, "//a [@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']//p [@class = 'counter_counter__num__3nue1']"]

class OrderPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[(text() = 'Конструктор')]")
    CREATE_ORDER_BUTTON = [By.XPATH, "//button[(text() = 'Оформить заказ')]"]
    MODAL_CLOSE_BUTTON = (By.XPATH, './/section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')
    ORDERS_TOTAL = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за все время:']]")
    ORDERS_TODAY = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за сегодня:']]")
    NUMBER_OF_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    ORDER_ID = [By.XPATH, ".//p[starts-with(@class, 'text text_type_digits-default')]"]
    LIST_NUMBER_OF_ORDER_ON_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")
    NUMBER_OF_ORDER_ON_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    CONSTRUCTOR_DROP = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    INGREDIENT = [By.XPATH, "//a [@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']"]
    LOADING = (By.XPATH, "//div [@class = 'Modal_modal_overlay__x2ZCr']")

class LoginPageLocators:
    EMAIL_LOCATOR = (By.XPATH, "//label[text() = 'Email']/parent::div/input")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@name = 'Пароль']")
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[text() = 'Войти']")
    LOADING = (By.CLASS_NAME, "Modal_modal__loading__3534A")



