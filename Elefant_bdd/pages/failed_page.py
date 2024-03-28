import time

from selenium.webdriver.common.by import By

from Sesiunea_14.Elefant_bdd.pages.base_page import BasePage


class FailedPage(BasePage):
    INPUT_EMAIL = (By.ID, 'ShopLoginForm_Login')
    INPUT_PASS = (By.ID, 'ShopLoginForm_Password')
    EXPECTED_URL = 'https://www.elefant.ro/my-account'
    INVALID_EMAIL = 'invalid'
    WRONG_EMAIL = 'wrong@testare.com'
    WRONG_PASS = 'wronggg'

    def input_invalid_credentials(self):
        self.type(self.INPUT_EMAIL, self.WRONG_EMAIL)
        self.type(self.INPUT_PASS, self.WRONG_PASS)
        time.sleep(1)
