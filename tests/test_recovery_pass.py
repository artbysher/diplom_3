import allure

import data
from curl import *
from pages.password_page import PasswordRecoveryPage


class TestsRecoverPass:
    @allure.title("Тест на переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description('Проверяем что URL страницы куда переходим после клика по кнопке "Востановить пароль" соответсвует ожидаемому URl')
    def test_transition_to_recover_password(self, driver):  # переход на страницу восстановления пароля по кнопке «Восстановить пароль»
        rec_pass = PasswordRecoveryPage(driver)
        rec_pass.click_to_main_page_btn()
        rec_pass.click_to_reset_pass_btn()
        assert driver.current_url == FORGOT_PASS_URL

    @allure.title("Тест на ввод почты и клик по кнопке «Восстановить»")
    @allure.description(
        'Проверяем что URL страницы куда переходим после заполнения email и клика по кнопке "Востановить" соответсвует ожидаемому URl')
    def test_transition_to_recover_password(self,driver):
        rec_pass = PasswordRecoveryPage(driver)
        rec_pass.click_to_main_page_btn()
        rec_pass.click_to_reset_pass_btn()
        rec_pass.send_email_to_rec_pass(data.Credentials.EMAIL)
        rec_pass.click_to_reset_btn()
        assert driver.current_url == RESET_PASS_URL

    @allure.title("Тест клик по кнопке показать/скрыть пароль")
    @allure.description(
        'Проверяем что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_transition_to_recover_password(self, driver):
        rec_pass = PasswordRecoveryPage(driver)
        rec_pass.main_page_loading_wait()
        rec_pass.click_to_main_page_btn()
        rec_pass.click_to_reset_pass_btn()
        rec_pass.send_email_to_rec_pass(data.Credentials.EMAIL)
        rec_pass.click_to_reset_btn()
        rec_pass.click_show_password_btn()

        assert rec_pass.check_show_password('input_type_text') and rec_pass.check_show_password('input_status_active')