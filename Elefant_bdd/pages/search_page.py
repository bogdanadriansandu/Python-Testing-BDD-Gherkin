import time

from selenium.webdriver.common.by import By

from Sesiunea_14.Elefant_bdd.pages.base_page import BasePage


class SearchPage(BasePage):
    LINK = 'https://www.elefant.ro/'
    ITEM = 'iphone 14'
    SEARCH_BOX = (By.NAME, 'SearchTerm')

    def navigate_to_home_page(self):
        self.navigate_to_page(self.LINK)
        time.sleep(2)

    def input_search_term(self):
        self.type(self.SEARCH_BOX, self.ITEM)

    def search_for_item(self):
        self.submit(self.SEARCH_BOX)
        time.sleep(2)
