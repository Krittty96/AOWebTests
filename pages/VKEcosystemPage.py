import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class VKEcosystemPageLocators:
    LOGO_VK = (By.XPATH, '//a[@id="header-logo"]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем наличие элементов на странице "Проекты" '):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.LOGO_VK)
