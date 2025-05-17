import allure

from curl import *
from pages.basic_function_page import BasicFunctionPage


class TestsBasicFunction:
    @allure.title("Тест на переход переход по клику на «Конструктор» из личного кабинета")
    @allure.description(
        'Проверяем что URL страницы куда переходим после клика по кнопке «Конструктор» соответсвует ожидаемому URl')
    def test_transition_to_constructor(self, authorize, driver):
        driver = authorize
        constructor = BasicFunctionPage(driver)
        constructor.click_to_lk_btn()
        constructor.click_to_constructor_btn()
        assert driver.current_url == MAIN_SITE

    @allure.title("Тест на переход переход по клику на «Лента заказов»а")
    @allure.description(
        'Проверяем что URL страницы куда переходим после клика по кнопке «Лента заказов» соответсвует ожидаемому URl')
    def test_transition_to_feed(self, driver):
        feed = BasicFunctionPage(driver)

        feed.click_to_feed_btn()
        assert driver.current_url == FEED_URL

    @allure.title("Тест на появление всплывающего окна с деталями об ингредиенте")
    @allure.description(
        'Проверяем что в появившемся после клика на ингредиент окне есть текст "Детали ингредиента"')
    def test_detail_window(self, driver):
        detail = BasicFunctionPage(driver)
        detail.click_to_ingredient_btn()
        window_text = detail.get_detail_window_text()

        assert "Детали ингредиента" in window_text and driver.current_url.startswith(INGREDIENT_URL)

    @allure.title("Тест на закрытие, окна с деталями об ингредиенте, через крестик")
    @allure.description(
            'Проверяем что всплывающее окно с деталями закрывается кликом по крестику')
    def  test_close_window(self, driver):
        function_page = BasicFunctionPage(driver)
        function_page.click_to_ingredient_btn()
        function_page.click_to_close_btn()

        top_text = function_page.get_element_text()

        assert "Начинки" in top_text

    @allure.title("Тест на изменение каунтера добавленного ингредиента")
    @allure.description(
            'Проверяем что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def  test_change_counter(self, driver):
        function_page = BasicFunctionPage(driver)
        function_page.put_ingredient_into_basket()
        counter_text = function_page.get_counter_text()

        assert "2" in counter_text


    @allure.title("Тест на оформление заказа авторизованныи пользователем")
    @allure.description(
        'Проверяем что URL страницы куда переходим после клика по кнопке «Конструктор» соответсвует ожидаемому URl')
    def test_create_order_auth(self, authorize, driver):
        driver = authorize
        function_page = BasicFunctionPage(driver)
        function_page.put_ingredient_into_basket()

        function_page.click_to_order_btn()
        order_text = function_page.get_id_order_text()
        assert "идентификатор заказа" in order_text




