from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_BUTTON = (By.XPATH, '//div[@class="toolbar_custom-logo_img-w __maslenitsa_2026_2"]')
    ECOSYSTEM_BUTTON = (By.XPATH, '//span[@class="toolbar_nav_i_ic"]')
    MORE_BUTTON = (By.XPATH, '//a[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем наличие всех необходимых элементов на странице'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.ECOSYSTEM_BUTTON)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f'Не удалось найти элемент {locator}')

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f'Не удалось найти элементы {locator}')

    @allure.step("Открываем страницу")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), 'скриншот', allure.attachment_type.PNG)

    @allure.step("Нажимаем кнопку экосистемы")
    def click_ecosystem(self):
        self.find_element(BasePageLocators.ECOSYSTEM_BUTTON).click()

    @allure.step("Нажимаем кнопку 'Ещё'")
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()

    @allure.step("Запоминаем индекс вкладки")
    def get_windows_id(self, index):
         return self.driver.window_handles[index]

    @allure.step("Переключаемся на соседнюю вкладку")
    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)

