from behave import Given, When, Then
import logging as logger


@Given("I am on the home page")
def on_the_home_page(context):
    print("Now on the homePage")


@When("I enter username and password")
def enter_username_password(context):
    print("valid username and password entered")


@When("I click on login button")
def click_login_button(context):
    print("login button clicked")


@Then("I should be logged")
def logged_in(context):
    print("Logged in successfully")