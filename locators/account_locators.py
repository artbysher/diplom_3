from selenium.webdriver.common.by import By


class AccountLocators:
    LK_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"]
    ORDER_HISTORY = [By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']"]
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")