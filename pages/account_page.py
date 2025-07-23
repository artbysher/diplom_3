import allure

from locators.account_locators import AccountLocators
from locators.base_locators import BaseLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Нажать на кнопку 'Личный кабинет' ")
    def click_to_lk_btn(self):
        locator = AccountLocators.LK_BUTTON
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)


    @allure.step("Нажать на  'История заказов' ")
    def click_to_order_history_btn(self):
        locator = AccountLocators.ORDER_HISTORY
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Нажать на  'Выход' в Личном кабинете ")
    def click_to_order_logout(self):
        locator = AccountLocators.LOGOUT_BUTTON
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)