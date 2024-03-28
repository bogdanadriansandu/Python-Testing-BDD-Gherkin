from behave import then


@then("I should see the correct title")
def step_impl(context):
    context.success_page.get_correct_title()


@then("I should see the correct url")
def step_impl(context):
    context.success_page.get_correct_url()
