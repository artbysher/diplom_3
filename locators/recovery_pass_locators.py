from selenium.webdriver.common.by import By


class RecPassLocators:
    RESET_PASS_BTN = [By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"]
    RESET_PASS_EMAIL = [By.XPATH, "//input[@name='name']"]
    RESET_BTN = [By.XPATH, "//button[text()='Восстановить']"]
    SHOW_PASS_BTN = [By.XPATH, '//div[@class="input__icon input__icon-action"]']
    PASS_PLACEHOLDER = [By.XPATH, '//label[text()="Пароль"]']
    HIDE_PASS_BTN = (By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]")
    SHOW_RESET_PASS_BTN = [By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_type_text') and contains(@class, 'input_status_active')]"]
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
