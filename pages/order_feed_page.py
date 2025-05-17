

import allure

from locators.account_locators import AccountLocators
from locators.base_locators import BaseLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Нажать на кнопку 'Лента заказов' ")
    def click_to_feed_btn(self):
        locator = OrderFeedLocators.FEED_BUTTON
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Нажать на первый заказ из списка ")
    def click_to_order_in_feed(self):
        locator = OrderFeedLocators.ORDER_IN_FEED
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Получить текст всплывающего окна")
    def get_order_window_text(self):
        return self.get_text_on_element(OrderFeedLocators.COMPOSITION)

    @allure.step("Всплывающее окно видно ")
    def get_order_window_is_displayed(self):
        return self.wait_for_element_is_displayed(OrderFeedLocators.ORDER_WINDOW)


    @allure.step("Перейти в историю заказов ' ")
    def get_to_order_history(self):
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(AccountLocators.LK_BUTTON)
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(AccountLocators.ORDER_HISTORY)

    @allure.step("Получим номер заказа' ")
    def get_to_order_number(self):
        locator = OrderFeedLocators.ORDER_NUM_HISTORY
        self.wait_for_element(locator)
        return self.find_element(locator).text

    @allure.step("Получить номер заказа в ленте заказов ")
    def get_element_text(self):
        locator = OrderFeedLocators.ORDER_NUMBER_FEED
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        return self.get_text_on_element(locator)

    @allure.step("Получить колличество заказов за все время ")
    def get_to_all_order(self):
        locator = OrderFeedLocators.ALL_ORDER
        return self.get_text_on_element(locator)

    @allure.step("Получить колличество заказов сегодня ")
    def get_to_today_order(self):
        locator = OrderFeedLocators.TODAY_ORDER
        return self.get_text_on_element(locator)

    @allure.step("Получить номер заказа при оформлении ")
    def get_number_create_order(self):
        locator = OrderFeedLocators.ORDER_CREATE_NUM
        self.get_order_number(OrderFeedLocators.MODAL)
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        return self.get_text_on_element(locator)

    @allure.step("Проверить номер заказа в разделе в работе  ")
    def get_number_order_in_work(self):
        locator = OrderFeedLocators.ORDER_IN_WORK
        order_in_work_list = self.get_text_on_element(locator)
        number = ''.join(order_in_work_list).lstrip('0')
        return number