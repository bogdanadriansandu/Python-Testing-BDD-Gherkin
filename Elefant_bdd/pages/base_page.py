from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Sesiunea_14.Elefant_bdd.driver import Driver


class BasePage(Driver):
    COOKIES = (By.CSS_SELECTOR, 'button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    def wait_for_visible_element(self, locator: tuple, ex_time=5):
        ex_wait = WebDriverWait(self.driver, ex_time)
        ex_wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable_element(self, locator: tuple, ex_time=5):
        ex_wait = WebDriverWait(self.driver, ex_time)
        ex_wait.until(EC.element_to_be_clickable(locator))

    def navigate_to_page(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(2)

        try:
            self.wait_for_clickable_element(self.COOKIES, 10)
            self.click(self.COOKIES)
        except Exception as e:
            pass

    def find(self, locator):
        self.wait_for_visible_element(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.wait_for_visible_element(locator)
        return self.driver.find_elements(*locator)

    def clear_type(self, locator, text):
        label = self.find(locator)
        label.clear()
        label.send_keys(text)

    def click(self, locator):
        self.wait_for_clickable_element(locator)
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def submit(self, locator):
        self.find(locator).submit()

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text

    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_value(text)

    def get_page_title(self):
        return self.driver.title

    def is_url_correct(self, expected_url):
        return expected_url == self.driver.current_url
