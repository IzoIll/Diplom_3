from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[(text() = 'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[(text() = 'Лента Заказов')]")
    POPUP_WINDOW = (By.XPATH, "//*[@id='root']/div/section[1]/div[1]/button")
    CLOSE_POPUP_BUTTON =  (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close__')]")
    INGREDIENT = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/img")
    CONSTRUCTOR_DROP = (By.XPATH, "//*[@id='root']/div/main/section[2]/ul")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p.text_type_digits-medium.mr-3")

class OrderPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//p[(text() = 'Лента Заказов')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[(text() = 'Конструктор')]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    MODAL_CLOSE_BUTTON = (By.XPATH, './/section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')
    ORDERS_TOTAL = (By.CSS_SELECTOR, "#root > div > main > div > div > div > div.undefined.mb-15 > p.OrderFeed_number__2MbrQ.text.text_type_digits-large")
    ORDERS_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    NUMBER_OF_ORDER = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2')
    LIST_NUMBER_OF_ORDER = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[1]/li[1]')
    CONSTRUCTOR_DROP = (By.XPATH, "//*[@id='root']/div/main/section[2]/ul")
    INGREDIENT = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/img")
    LOADING = (By.CSS_SELECTOR, "img[src*='loading'][alt='loading animation']")

class LoginPageLocators:
    EMAIL_LOCATOR = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_LOCATOR = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Войти']")
    LOADING = (By.CSS_SELECTOR, "img[src*='loading'][alt='loading animation']")



