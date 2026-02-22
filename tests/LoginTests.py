import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = "Введите логин"
ENPTY_PASSWORD_ERROR = "Введите пароль"

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки  при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустом поле'Пароль'")
def test_login_and_not_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_login(LoginPage.generator_random_login(8))
    LoginPage.click_login()
    assert LoginPageHelper(browser).get_error_text() == ENPTY_PASSWORD_ERROR

