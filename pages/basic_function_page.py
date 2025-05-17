import allure

from locators.account_locators import AccountLocators
from locators.base_locators import BaseLocators
from locators.basic_function_locators import BasicFunctionLocators
from pages.base_page import BasePage


class BasicFunctionPage(BasePage):
    @allure.step("Нажать на кнопку 'Личный кабинет' ")
    def click_to_lk_btn(self):
        locator = AccountLocators.LK_BUTTON
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Нажать на кнопку 'Конструктор' ")
    def click_to_constructor_btn(self):
        locator = BasicFunctionLocators.CONSTRUCTOR_BUTTON
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Нажать на кнопку 'Лента заказов' ")
    def click_to_feed_btn(self):
        locator = BasicFunctionLocators.FEED_BUTTON
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Нажать на ингридиент 'Краторная булка N-200i' ")
    def click_to_ingredient_btn(self):
        locator = BasicFunctionLocators.INGREDIENT_BUN
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Получить текст всплывающего окна")
    def get_detail_window_text(self):
        return self.get_text_on_element(BasicFunctionLocators.DETAIL_INGREDIENT)

    @allure.step("Закрыть всплывающее окно по клику на крестик ")
    def click_to_close_btn(self):
        locator = BasicFunctionLocators.CLOSE_BTN
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.wait_for_element(locator)
        self.click_on_element(locator)

    @allure.step("Получить текст 'Начинки'")
    def get_element_text(self):
        return self.get_text_on_element(BasicFunctionLocators.TOPPING)

    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self):
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        ingredient = self.wait_for_element(locator=BasicFunctionLocators.INGREDIENT_BUN)
        basket = self.wait_for_element(locator=BasicFunctionLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Получить значение каунтера")
    def get_counter_text(self):
        return self.get_text_on_element(BasicFunctionLocators.COUNTER_BUN)

    @allure.step("Нажать на кнопку 'Оформить заказ' ")
    def click_to_order_btn(self):
        locator = BasicFunctionLocators.ORDER_BTN
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Получить значение каунтера")
    def get_id_order_text(self):
        return self.get_text_on_element(BasicFunctionLocators.ID_ORDER)