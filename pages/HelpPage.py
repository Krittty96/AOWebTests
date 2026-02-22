import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class HelpPageLocators:
    RELEVANT_TODAY_BUTTON = (By.XPATH, '//span[@data-icon-name="illustrations/ill_actual"]')
    REGISTRATION_BUTTON = (By.XPATH, '//span[@name="illustrations/ill_registration"]')
    MY_PROFILE_BUTTON = (By.XPATH,'//a[@href="/help/moi-profil"]')
    COMMUNICATION_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_communication"]')
    ACCESS_TO_PROFILE_BUTTON = (By.XPATH,'//a[@href="/help/dostup-k-profilu"]')
    SAFETY_BUTTON= (By.XPATH,'//span[@data-icon-name="illustrations/ill_security"]')
    GROUPS_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_group_group"]')
    PAID_FEATURES_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_paid_features"]')
    VIOLATION_AND_SPAM_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_violation_spam"]')
    GAMES_AND_APPLICATIONS_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_app_game"]')
    OTHER_SERVICES_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_other_services"]')
    USEFUL_INFORMATION_BUTTON = (By.XPATH,'//span[@data-icon-name="illustrations/ill_useful_info"]')
    ADVERTISING_OFFICE_BUTTON = (By.XPATH,'//span[@name="illustrations/ill_advertising_cabinet"]')

class HelpPageHelper(BasePageHelper):
        def __init__(self, driver):
            self.driver = driver
            self.check_page()

        def check_page(self):
            with allure.step('Проверяем наличие элементов на странице "Помощь"'):
                self.attach_screenshot()
            self.find_element(HelpPageLocators.REGISTRATION_BUTTON)
            self.find_element(HelpPageLocators.REGISTRATION_BUTTON)
            self.find_element(HelpPageLocators.MY_PROFILE_BUTTON)
            self.find_element(HelpPageLocators.COMMUNICATION_BUTTON)
            self.find_element(HelpPageLocators.ACCESS_TO_PROFILE_BUTTON)
            self.find_element(HelpPageLocators.SAFETY_BUTTON)
            self.find_element(HelpPageLocators.GROUPS_BUTTON)
            self.find_element(HelpPageLocators.PAID_FEATURES_BUTTON)
            self.find_element(HelpPageLocators.VIOLATION_AND_SPAM_BUTTON)
            self.find_element(HelpPageLocators.GAMES_AND_APPLICATIONS_BUTTON)
            self.find_element(HelpPageLocators.OTHER_SERVICES_BUTTON)
            self.find_element(HelpPageLocators.USEFUL_INFORMATION_BUTTON)
            self.find_element(HelpPageLocators.ADVERTISING_OFFICE_BUTTON)

        def scrollToitem(self, locator):
            scroll_item = self.find_element(locator)
            ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()