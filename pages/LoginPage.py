import random
import string

import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_CODE_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    PASSWORD_DISPLAY_BUTTON = (By.XPATH, '//div[@class ="vkuiFormField__iconWrapper"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]//span[@class="vkuiButton__in"]')
    LOGIN_QR_CODE_BUTTON = (By.XPATH,
                            '//div[@class="LoginForm-module__root___-Bijm"]//button[@type="button"]//span[@class="vkuiButton__in"]')
    RESTORE_ACCESS_BUTTON = (By.XPATH,
                             '//*[@class="common-module__centered___tKWXI vkuiSubhead__host vkuiSubhead__sizeYNone vkuiTypography__host vkuiTypography__normalize vkuiTypography__weight2 vkuiRootComponent__host"]/button')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="LoginFormMain-module__bottom___YLtCo"]//button')
    VK_AUTHENTICATION_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_AUTHENTICATION_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_AUTHENTICATION_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')

    RESTORE_BUTTON = (By.XPATH,'//div[@class="RecoveryMain-module__root___ff337"]//a//span[@class="vkuiButton__content"]')
    CANCEL_BUTTON = (By.XPATH, '//div[@class="RecoveryMain-module__root___ff337"]//button')

    ERROR = (By.XPATH,
             '//*[@class="LoginForm-module__error___1xmAD vkuiCaption__sizeYNone vkuiCaption__level1 vkuiTypography__host vkuiTypography__normalize vkuiRootComponent__host"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем наличие элементов на странице авторизации'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_DISPLAY_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.RESTORE_ACCESS_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_AUTHENTICATION_BUTTON)
        self.find_element(LoginPageLocators.MAIL_AUTHENTICATION_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_AUTHENTICATION_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_TAB)
        self.find_element(LoginPageLocators.LOGIN_TAB)


    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR).text

    @allure.step("Заполняем поле логин")
    def enter_login(self,login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()


    def generator_random_login(self,length=12):
        chars=string.ascii_letters+string.digits
        return ''.join(random.choices(chars,k=length))

    @allure.step("Заполняем поле пароль")
    def enter_password(self,password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    def generator_random_password(self,length=12):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    @allure.step("Переходим к форме восстановления")
    def click_recovery (self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_BUTTON).click()

    @allure.step("Переходим к регистрации аккаунта")
    def click_registration (self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()