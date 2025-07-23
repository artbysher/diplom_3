
import allure

from locators.base_locators import BaseLocators
from locators.recovery_pass_locators import RecPassLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step("Нажать на кнопку 'Войти в аккаунт' ")
    def click_to_main_page_btn(self):
        locator = BaseLocators.MAIN_PAGE_BUTTON
        self.click_on_element(locator)


    @allure.step("Нажать на кнопку 'Востановить пароль' ")
    def click_to_reset_pass_btn(self):
        locator = RecPassLocators.RESET_PASS_BTN
        self.click_on_element( locator)

    @allure.step("Заполнить поле email в форме востановления пароля")
    def send_email_to_rec_pass(self, email):
        locator = RecPassLocators.RESET_PASS_EMAIL
        self.click_on_element(locator)
        self.send_keys_to_input(locator, email)

    @allure.step("Нажать на кнопку 'Востановить' ")
    def click_to_reset_btn(self):
        locator = RecPassLocators.RESET_BTN
        pass_locator = RecPassLocators.PASS_PLACEHOLDER
        self.click_on_element(locator)
        self.wait_for_element(pass_locator)

    @allure.step("Нажимаем кнопку Показать/спрятать пароль")
    def click_show_password_btn(self):
        locator = RecPassLocators.HIDE_PASS_BTN
        self.wait_for_element_hide(BaseLocators.OVERLAY)
        self.click_on_element(locator)

    @allure.step("Проверяем что поле подсветилось, и появились новые атрибуты в классе")
    def check_show_password(self, actual_classes):
        locator = RecPassLocators.SHOW_RESET_PASS_BTN
        return actual_classes in self.find_element(locator).get_attribute(
            'class')

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(BaseLocators.OVERLAY)