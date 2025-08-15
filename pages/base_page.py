from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def find_elements(self, elements):
        return self.driver.find_element(*elements)

    def click_on_element(self, element):
        self.find_elements(element).click()

    def click_on_ingredient(self):
        self.find_elements(locators.OrderPageLocators.INGREDIENT).click()

    def get_cur_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def close_element_with_wait(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def fill_element(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)