import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage  import HelpPageHelper , HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка содержимого страницы "Помощь"')
@allure.title('Проверка раздела "Рекламный кабинет"')
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISING_OFFICE_BUTTON)
    AdvertisementCabinetHelpHelper(browser)
