import pytest
from selenium import webdriver


from curl import *
from data import Credentials
from locators.base_locators import BaseLocators


#@pytest.fixture(scope="function")

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(MAIN_SITE)
    elif request.param == "firefox":
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get(MAIN_SITE)
    yield browser
    browser.quit()


@pytest.fixture
def authorize(driver):
    #Фикстура для авторизации пользователя.
    driver.find_element(*BaseLocators.MAIN_PAGE_BUTTON).click()
    driver.find_element(*BaseLocators.EMAIL).send_keys(Credentials.EMAIL)
    driver.find_element(*BaseLocators.PASSWORD).send_keys(Credentials.PASSWORD)
    driver.find_element(*BaseLocators.LOGIN_BUTTON).click()
    return driver