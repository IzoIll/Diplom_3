from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop
import allure
from locators import LoginPageLocators, OrderPageLocators
from pages.base_page import BasePage
from urls import *
import time

class OrderPage(BasePage):

    @allure.step('Клик на кнопку Лента заказов')
    def click_on_feed_button(self):
        self.click_on_element(OrderPageLocators.ORDER_FEED_BUTTON)
        self.wait.until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDERS_TOTAL))

    @allure.step('Клик на кнопку Конструктор')
    def click_on_constructor_button(self):
        self.click_on_element(OrderPageLocators.CONSTRUCTOR_BUTTON)
        self.wait.until(expected_conditions.url_contains(MAIN_URL))

    @allure.step('Клик на кнопку Конструктор')
    def click_on_order_button(self):
        self.click_on_element(OrderPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Клик на кнопку Закрыть окно заказа')
    def click_on_close_window_button(self):
        time.sleep(3)
        self.click_on_element(OrderPageLocators.MODAL_CLOSE_BUTTON)
        self.wait.until(expected_conditions.url_contains(MAIN_URL))

    @allure.step("Получить общее количество заказов")
    def get_total_orders(self):
        time.sleep(3)
        return self.find_elements(OrderPageLocators.ORDERS_TOTAL).text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        time.sleep(3)
        return self.find_elements(OrderPageLocators.ORDERS_TODAY).text

    @allure.step('Получение номера в окне о создании заказа')
    def get_number_of_order(self):
        time.sleep(3)
        return self.find_elements(OrderPageLocators.NUMBER_OF_ORDER).text

    @allure.step('Получение списка номеров заказов')
    def get_list_number_of_order(self):
        return self.find_elements(OrderPageLocators.LIST_NUMBER_OF_ORDER).text

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.wait.until(expected_conditions.url_to_be(MAIN_URL))
        ingredient = self.find_element_with_wait(OrderPageLocators.INGREDIENT)
        basket = self.find_element_with_wait(OrderPageLocators.CONSTRUCTOR_DROP)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Логин в систему')
    def login(self, email, password):
        self.driver.get(URL_LOGIN)
        self.fill_element(LoginPageLocators.EMAIL_LOCATOR, email)
        self.fill_element(LoginPageLocators.PASSWORD_LOCATOR, password)
        self.close_element_with_wait(OrderPageLocators.LOADING)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON_LOCATOR)
        self.close_element_with_wait(OrderPageLocators.LOADING)
        return