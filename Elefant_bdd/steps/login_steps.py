from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I enter a valid email address and password")
def step_impl(context):
    context.login_page.input_valid_credentials()


@when("I click on 'CONECTARE' button")
def step_impl(context):
    context.login_page.click_login_button()


@when("I enter the wrong {email_address} and {password}")
def step_impl(context, email_address, password):
    pass


@when("I enter an invalid email address")
def step_impl(context):
    pass
