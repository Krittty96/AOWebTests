
import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH,'//a[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH,'//a[@data-l="t,email"]')
    QR_CODE = (By.XPATH,'//img[@class="qr_code_image"]')
    SUPPORT_LINK = (By.XPATH,'//div[@class="support-link_item-text"]')


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем наличие элементов на странице восстановления доступа'):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_LINK)