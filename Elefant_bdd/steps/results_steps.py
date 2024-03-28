from behave import then


@then("I should see more than 10 results displayed")
def step_impl(context):
    results = context.results_page.count_results()
    assert results >= 10, 'Mai putin de 10 rezultate gasite'
