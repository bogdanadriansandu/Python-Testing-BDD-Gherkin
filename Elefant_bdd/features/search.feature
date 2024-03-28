Feature: Search functionality

  @search_item
  Scenario: Search for an item
    Given I am on the home page
    When I enter an item in the search box
    And I submit the search form
    Then I should see more than 10 results displayed