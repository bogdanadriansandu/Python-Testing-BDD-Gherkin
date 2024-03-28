from Sesiunea_14.Elefant_bdd.driver import Driver
from Sesiunea_14.Elefant_bdd.pages.failed_page import FailedPage
from Sesiunea_14.Elefant_bdd.pages.login_page import LoginPage
from Sesiunea_14.Elefant_bdd.pages.results_page import ResultsPage
from Sesiunea_14.Elefant_bdd.pages.search_page import SearchPage
from Sesiunea_14.Elefant_bdd.pages.success_page import SuccessPage


def before_all(context):
    context.driver = Driver()
    context.login_page = LoginPage()
    context.success_page = SuccessPage()
    context.failed_page = FailedPage()
    context.search_page = SearchPage()
    context.results_page = ResultsPage()


def after_all(context):
    context.driver.close_driver()
