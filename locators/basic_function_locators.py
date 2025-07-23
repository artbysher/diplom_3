from selenium.webdriver.common.by import By


class BasicFunctionLocators:
    CONSTRUCTOR_BUTTON = [By.XPATH, "//p[text()='Конструктор']"]
    FEED_BUTTON = [By.XPATH, "//p[text()='Лента Заказов']"]

    INGREDIENT_BUN = [By.XPATH, "//img[@alt='Краторная булка N-200i']"]
    DETAIL_INGREDIENT = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    CLOSE_BTN = [By.XPATH,"//button[contains(@class, 'modal__close')]"]
    TOPPING = [By.XPATH, "//span[text()='Начинки']"]
    BASKET = [By.XPATH,'//section[contains(@class, "BurgerConstructor_basket")]']
    COUNTER_BUN =[By.XPATH,'(//p[contains(@class, "counter_counter__num__3nue1")])[2]']
    ORDER_BTN = [By.XPATH,"//button[text()='Оформить заказ']"]
    ID_ORDER = [By.XPATH,"//p[text()='идентификатор заказа']"]