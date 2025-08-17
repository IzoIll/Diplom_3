from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
import allure
import locators
from urls import *

class MainPage(BasePage):

    @allure.step('Открытие страницы логина')
    def open_login_page(self):
        self.driver.get(URL_LOGIN)
        self.wait.until(expected_conditions.url_to_be(URL_LOGIN))

    @allure.step('Открытие страницы конструктора')
    def open_main_page(self):
        self.driver.get(MAIN_URL)
        self.wait.until(expected_conditions.url_to_be(MAIN_URL))

    @allure.step('Клик на кнопку Конструктор')
    def click_to_open_constructor_page(self):
        self.click_on_element(locators.MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait.until(expected_conditions.url_contains(MAIN_URL))

    @allure.step('Клик на кнопку Лента заказов')
    def click_on_order_button(self):
        self.click_on_element(locators.MainPageLocators.ORDER_FEED_BUTTON)
        self.wait.until(expected_conditions.url_contains(URL_FEED))

    @allure.step('Клик на кнопку закрытия попапа')
    def click_on_close_popup_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(locators.MainPageLocators.CLOSE_POPUP_BUTTON))
        self.click_on_element(locators.MainPageLocators.CLOSE_POPUP_BUTTON)
        self.wait.until(expected_conditions.invisibility_of_element_located(locators.MainPageLocators.CLOSE_POPUP_BUTTON))

    @allure.step('Проверка состояния окна попапа')
    def check_popup_window(self):
        return self.find_elements(locators.MainPageLocators.POPUP_WINDOW).is_displayed()

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        return self.find_elements(locators.MainPageLocators.INGREDIENT_COUNTER).text

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.wait.until(expected_conditions.url_to_be(MAIN_URL))
        ingredient = self.find_element_with_wait(locators.MainPageLocators.INGREDIENT)
        basket = self.find_element_with_wait(locators.MainPageLocators.CONSTRUCTOR_DROP)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Ожидание изменения текста')
    def wait_chainge_text(self, text):
        self.wait.until(expected_conditions.text_to_be_present_in_element(locators.MainPageLocators.INGREDIENT_COUNTER, text))