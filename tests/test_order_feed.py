import allure

from pages.basic_function_page import BasicFunctionPage
from pages.order_feed_page import OrderFeedPage


class TestsOrderFeed:
    @allure.title("Тест на появление всплывающего окна с деталями заказа")
    @allure.description(
        'Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_window(self, authorize, driver):
        driver = authorize
        order_feed = OrderFeedPage(driver)
        order_feed.click_to_feed_btn()
        order_feed.click_to_order_in_feed()
        window_text = order_feed.get_order_window_text()

        assert 'Cостав' in window_text and order_feed.get_order_window_is_displayed() ==True


    @allure.title("Тест заказ из «Истории заказов» отображаются в «Ленте заказов» ")
    @allure.description(
        'Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_in_feed(self, authorize, driver):
        driver = authorize
        function_page = BasicFunctionPage(driver)
        function_page.put_ingredient_into_basket()
        function_page.click_to_order_btn()
        function_page.click_to_close_btn()

        order_feed = OrderFeedPage(driver)
        order_feed.get_to_order_history()
        order_number = order_feed.get_to_order_number()
        order_feed.click_to_feed_btn()
        top_text = order_feed.get_element_text()

        assert order_number in top_text

    @allure.title("Тест на увеличение значения счетчика «Выполнено за всё время» при создании нового заказа ")
    @allure.description(
        'Проверяем что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_all_order(self, authorize, driver):
        driver = authorize
        order_feed = OrderFeedPage(driver)
        order_feed.click_to_feed_btn()
        all_order = order_feed.get_to_all_order()

        function_page = BasicFunctionPage(driver)
        function_page.click_to_constructor_btn()
        function_page.put_ingredient_into_basket()
        function_page.click_to_order_btn()
        function_page.click_to_close_btn()

        order_feed = OrderFeedPage(driver)
        order_feed.click_to_feed_btn()
        new_all_order = order_feed.get_to_all_order()


        assert new_all_order >= all_order

    @allure.title("Тест на увеличение значения счетчика «Выполнено за сегодня» при создании нового заказа ")
    @allure.description(
        'Проверяем что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_order(self, authorize, driver):
        driver = authorize
        order_feed = OrderFeedPage(driver)
        order_feed.click_to_feed_btn()
        today_order = order_feed.get_to_today_order()

        function_page = BasicFunctionPage(driver)
        function_page.click_to_constructor_btn()
        function_page.put_ingredient_into_basket()
        function_page.click_to_order_btn()
        function_page.click_to_close_btn()

        order_feed = OrderFeedPage(driver)
        order_feed.click_to_feed_btn()
        new_today_order = order_feed.get_to_today_order()

        assert new_today_order >= today_order

    @allure.title("Тест на появление номер а в разделе «В работе»")
    @allure.description(
        'Проверяем что после оформления заказа его номер появляется в разделе В работе.')
    def test_order_in_work(self, authorize, driver):
        driver = authorize
        function_page = BasicFunctionPage(driver)
        function_page.click_to_constructor_btn()
        function_page.put_ingredient_into_basket()
        function_page.click_to_order_btn()

        order_feed = OrderFeedPage(driver)
        order_number = order_feed.get_number_create_order()

        function_page = BasicFunctionPage(driver)
        function_page.click_to_close_btn()

        order_feed = OrderFeedPage(driver)
        order_feed.click_to_feed_btn()
        order_in_work = order_feed.get_number_order_in_work()

        assert order_number == order_in_work





