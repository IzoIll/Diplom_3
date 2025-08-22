import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import locators

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    @allure.step('Поиск элемента')
    def find_elements(self, elements):
        return self.driver.find_element(*elements)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        click = ActionChains(self.driver)
        click.move_to_element(WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))).click().perform()

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self):
        self.find_elements(locators.OrderPageLocators.INGREDIENT).click()

    @allure.step('Узнать текущий адрес страницы')
    def get_cur_url(self):
        return self.driver.current_url

    @allure.step('Подождать загрузки страницы и найти элемент')
    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание закрытия элемента')
    def close_element_with_wait(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Заполнить строку ввода')
    def fill_element(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)