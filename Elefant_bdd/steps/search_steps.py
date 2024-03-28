from behave import given, when


@given("I am on the home page")
def step_impl(context):
    context.search_page.navigate_to_home_page()


@when("I enter an item in the search box")
def step_impl(context):
    context.search_page.input_search_term()


@when("I submit the search form")
def step_impl(context):
    context.search_page.search_for_item()
