from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@when("I click on GO")
def step_imp(context):
    link = context.browser.find_element(By.ID, "submit")
    link.click()


