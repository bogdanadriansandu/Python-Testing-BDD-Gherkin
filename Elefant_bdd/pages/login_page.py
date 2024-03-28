import time

from selenium.webdriver.common.by import By

from Sesiunea_14.Elefant_bdd.pages.base_page import BasePage


class LoginPage(BasePage):
    LINK = 'https://www.elefant.ro/login'
    EMAIL = 'bopad94366@bitofee.com'
    PASSWORD = 'testare123'
    INPUT_EMAIL = (By.ID, 'ShopLoginForm_Login')
    INPUT_PASS = (By.ID, 'ShopLoginForm_Password')
    LOGIN_BUTTON = (By.NAME, 'login')

    def navigate_to_login_page(self):
        self.navigate_to_page(self.LINK)
        time.sleep(2)

    def input_valid_credentials(self):
        self.type(self.INPUT_EMAIL, self.EMAIL)
        self.type(self.INPUT_PASS, self.PASSWORD)
        time.sleep(1)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)
