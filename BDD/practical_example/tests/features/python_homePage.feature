# Created by echalo at 21/06/2020
Feature: Navigation bars int he home page

  Scenario: Verify the navigation bars on home page are visible

    Given I go to the homepage
    Then the page title should be "Welcome to Python.org"
    Given I click on GO
    Then I should see text "Search Python.org"