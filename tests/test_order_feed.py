from pages.order_page import OrderPage
from data import UsersTestData
import allure

class TestOrderFeed:

    @allure.title("Увеличение счетчиков заказов за все время")
    def test_go_to_order_total(self, driver):
        order_feed_page = OrderPage(driver)
        order_feed_page.login(UsersTestData.email, UsersTestData.password)
        order_feed_page.click_on_feed_button()
        first = order_feed_page.get_total_orders()
        order_feed_page.click_on_constructor_button()
        order_feed_page.put_ingredient_into_basket()
        order_feed_page.click_on_order_button()
        order_feed_page.open_feed_page()
        second = order_feed_page.get_total_orders()
        assert first < second

    @allure.title("Увеличение счетчиков заказов за сегодня")
    def test_go_to_order_today(self, driver):
        order_feed_page = OrderPage(driver)
        order_feed_page.login(UsersTestData.email, UsersTestData.password)
        order_feed_page.click_on_feed_button()
        first = order_feed_page.get_today_orders()
        order_feed_page.click_on_constructor_button()
        order_feed_page.put_ingredient_into_basket()
        order_feed_page.click_on_order_button()
        order_feed_page.open_feed_page()
        second = order_feed_page.get_today_orders()
        assert first < second


    @allure.title("Заказ в работе")
    def test_is_order_in_progress(self, driver):
        order_feed_page = OrderPage(driver)
        order_feed_page.login(UsersTestData.email, UsersTestData.password)
        order_feed_page.click_on_constructor_button()
        order_feed_page.put_ingredient_into_basket()
        order_feed_page.click_on_order_button()
        order_id = order_feed_page.get_number_of_order()
        order_feed_page.open_feed_page()
        assert order_feed_page.get_list_number_of_order() == '0' + order_id