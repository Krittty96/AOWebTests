import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper


BASE_URL = 'https://ok.ru/'

@allure.suite("Проверка формы восстановления доступа к аккаунту")
@allure.title("Проверка перехода к форме восстановления доступа после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_login(LoginPage.generator_random_login(8))
    Password = LoginPage.generator_random_password(4)

    for i  in range(3):
        LoginPage.enter_password(Password)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)




