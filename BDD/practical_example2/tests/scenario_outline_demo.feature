# Created by echalo at 23/06/2020
Feature: example/demo of scenario outline


  Scenario Outline: Users in with shipping address in <state> should get charged sales tax

    Given I login as a new user
    When I add a "$40" book to the cart
    And I add a "<state>" shipping address
    Then tax should be calculated

    Examples:
      | state |
      |  CA   |
      |  NY   |
      |  TX   |






Feature:  Create user with bad password

  Scenario Outline:  try password “<type>”

    Given I am at create user page
    When I type “<type>” password
    Then I should see error message

    Examples:
      | type         |
      | too long     |
      | too short    |
      | all numbers  |
      | all letters  |
