from selenium.webdriver.common.by import By

from Sesiunea_14.Elefant_bdd.pages.base_page import BasePage


class ResultsPage(BasePage):
    RESULTS = (By.CSS_SELECTOR, '.product-title')

    def count_results(self):
        counter = self.find_elements(self.RESULTS)
        return len(counter)
