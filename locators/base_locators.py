from selenium.webdriver.common.by import By


class BaseLocators:
    # Локаторы для входа
    EMAIL = [By.XPATH, "//input[@name='name']"]
    PASSWORD = [By.XPATH, "//input[@name='Пароль']"]
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка на стартовом экране "Войти в акккаунт"
    ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    REG_LOG_BUTTON = [By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']"]
    RESET_PASS_BUTTON = [By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"]
