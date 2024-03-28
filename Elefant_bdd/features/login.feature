Feature: Login functionality

  Background:
    Given I am on the login page

  @login_successfully
  Scenario: Login successfully
    When I enter a valid email address and password
    And I click on 'CONECTARE' button
    Then I should see the correct title
    And I should see the correct url

  @login_failed
  Scenario Outline: Login failed wrong credentials
    When  I enter the wrong <email_address> and <password>
    And I click on 'CONECTARE' button
    Then I can not login
    And I should receive an error message

  Examples:
    | email_address    | password |
    | gresita@test.com | gresita  |
    | eronata@test.com | eronata  |
    
  @login_failed
  Scenario: Login failed empty fields
    When  I click on 'CONECTARE' button
    Then I should be on the same page
    And I should receive an empty fields error message

  @login_failed
  Scenario: Login failed invalid email address
    When I enter an invalid email address
    Then I should receive an invalid email error message
    And The 'CONECTARE' button should be disabled
