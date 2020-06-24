from behave import given, when, then


@given("I login as a new user")
def step_impl(context):
    print("I am logged in as a new user")


@when('I add a "{amount}" book to the cart')
def step_impl(context, amount):
    print("amount added")


@when('I add a "{state}" shipping address')
def step_impl(context, state):
    print("Adding address in state: {}".format(state))


@then("tax should be calculated")
def step_impl(context):
    print("tax is calculated")
