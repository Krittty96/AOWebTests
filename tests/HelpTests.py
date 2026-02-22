import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage  import HelpPageHelper , HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка содержимого страницы "Помощь"')
@allure.title('Проверка раздела "Рекламный кабинет"')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISING_OFFICE_BUTTON)
    AdvertisementCabinetHelpHelper(browser)
