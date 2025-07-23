import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop



class BasePage:
    def __init__(self, driver):
           self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()


    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Наити элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)


    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text


    @allure.step("Сравнить текущий URL с ожидаемым")
    def check_url(self, expected_url):
        actual_url = self.driver.current_url
        return actual_url == expected_url


    @allure.step("Подождать ожидаемый URL страницы")
    def wait_for_url(self, expected_url, timeout=10):
        return (WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url)))


    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Подождать видимости элемента")
    def wait_for_element_is_displayed(self, locator):
        element = self.wait_for_element(locator)
        return  element.is_displayed()

    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидать видимости номера")
    def get_order_number(self, locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

