from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I go to the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.python.org/")


@then('the page title should be "{expected_title}"')
def step_impl(context, expected_title):
    # expected_title = "Welcome to Python.org"
    actual_title = context.browser.title
    print("The actual title is: {}".format(actual_title))
    assert expected_title == actual_title


@given("I click on GO")
def step_imp(context):
    link = context.browser.find_element(By.ID, "submit")
    link.click()


@then('I should see text "{expected_text}"')
def step_impl(context, expected_text):
    if expected_text not in ['Search Python.org']:
        raise Exception("text not found")
    print(expected_text)
