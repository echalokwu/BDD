# Created by echalo at 18/06/2020
Feature: testing login

  Scenario: login test
    Given I am on the home page
    When I enter username and password
    When I click on login button
    Then I should be logged

