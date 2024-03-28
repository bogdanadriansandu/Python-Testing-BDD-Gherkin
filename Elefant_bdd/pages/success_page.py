from Sesiunea_14.Elefant_bdd.pages.base_page import BasePage


class SuccessPage(BasePage):
    EXPECTED_URL = 'https://www.elefant.ro/my-account'
    PAGE_TITLE = 'Contul Meu'

    def get_correct_title(self):
        actual_title = self.get_page_title()
        assert self.PAGE_TITLE == actual_title, 'Eroare titlu pagina'

    def get_correct_url(self):
        assert self.is_url_correct(self.EXPECTED_URL)
