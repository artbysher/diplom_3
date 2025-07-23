import allure

from curl import *
from pages.account_page import AccountPage


class TestsAccount:
    @allure.title("Тест на переход переход по клику на «Личный кабинет»")
    @allure.description('Проверяем что URL страницы куда переходим после клика по кнопке "Личный кабинет" соответсвует ожидаемому URl')
    def test_transition_to_personal_account(self, driver):
        lk = AccountPage(driver)
        lk.click_to_lk_btn()

        assert lk.check_url(LOGIN_URL)

    @allure.title("Тест на переход переход по клику на «История заказов» из личного кабинета")
    @allure.description(
        'Проверяем что URL страницы куда переходим после клика по кнопке "История заказов" соответсвует ожидаемому URl')
    def test_transition_to_order_history(self, authorize, driver):
        driver = authorize
        lk = AccountPage(driver)
        lk.click_to_lk_btn()
        lk.click_to_order_history_btn()
        assert lk.check_url(ORDER_HISTORY_URL)

    @allure.title("Тест на выход из Личного кабинета ")
    @allure.description(
        'Проверяем что URL после нажатия на кнопку "выход" соответсвует ожидаемому URl')
    def test_transition_to_logout(self, authorize, driver):
        driver = authorize
        lk = AccountPage(driver)
        lk.click_to_lk_btn()

        lk.click_to_order_logout()
        lk.wait_for_url(LOGIN_URL)
        assert lk.check_url(LOGIN_URL)

