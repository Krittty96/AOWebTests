import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random


class RegistrationPageLocators:
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRIES_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    NUMBER_PHONE = (By.XPATH, '//input[@id="field_phone"]')
    NEXT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_LINK = (By.XPATH, '//a[@data-l="t,support"]')
    REGULATIONS_LINK = (By.XPATH, '//a[@data-l="t,agreement"]')
    PRIVACY_POLICY_LINK = (By.XPATH, '//a[@data-l="t,privacy"]')


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем наличие элементов на странице регистрации'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.NUMBER_PHONE)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.NEXT_BUTTON)
        self.find_element(RegistrationPageLocators.SUPPORT_LINK)
        self.find_element(RegistrationPageLocators.REGULATIONS_LINK)
        self.find_element(RegistrationPageLocators.PRIVACY_POLICY_LINK)


@allure.step('Выбираем рандомную страну/регион')
def select_random_country(self):
    random_number = random.randint(0, 212)
    self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
    country_items = self.find_elements(RegistrationPageLocators.COUNTRIES_ITEM)
    country_code = country_items[random_number].get_attribute('text')
    country_items[random_number].click()
    return country_code

@allure.step('Проверяем соответствие кода телефона выбранной страны ожидаемому')
def get_phone_field_value(self):
    return self.find_element(RegistrationPageLocators.NUMBER_PHONE).get_attribute("text")
