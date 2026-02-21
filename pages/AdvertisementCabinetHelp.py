from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure




class AdvertisementCabinetHelpLocators:
    TITLE = (By.XPATH, '//span[text()= "Рекламный кабинет"]')

class AdvertisementCabinetHelpHelper(BasePage) :
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step("Проверяем наличие обязательных элементов на странице 'Рекламный кабинет'"):
            self.attach_screenshot()
        self.find_element(AdvertisementCabinetHelpLocators.TITLE)