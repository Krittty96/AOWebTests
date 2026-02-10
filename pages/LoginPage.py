from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    PASSWORD_DISPLAY_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-3485194480"]/vkid-form-adapter/div/div/div/div[1]/form/div[2]/span/div/div[2]/span/button')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-3485194480"]/vkid-form-adapter/div/div/div/div[1]/form/button')
    LOGIN_QR_CODE_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-3485194480"]/vkid-form-adapter/div/div/div/div[1]/button')
    RESTORE_ACCESS_BUTTON= (By.XPATH,'//*[@id="tabpanel-login-6342642218"]/vkid-form-adapter/div/div/div/div[1]/span/button')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-6342642218"]/vkid-form-adapter/div/div/div/div[3]/button')
    VK_AUTHENTICATION_BUTTON = (By.XPATH,'//*[@data-l="t,vkc"]')
    MAIL_AUTHENTICATION_BUTTON= (By.XPATH,'//*[@data-l="t,mailru"]')
    YANDEX_AUTHENTICATION_BUTTON = (By.XPATH,'//*[@data-l="t,yandex"]')
    LOGIN_TAB = (By.XPATH,'//*[@data-l="t,login_tab"]')
    QR_CODE_TAB = (By.XPATH,'//*[@data-l="t,qr_tab"]')


class LoginPageHelper(BasePage):
    pass