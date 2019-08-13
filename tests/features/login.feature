# Feature for home page

Feature: As a end user,
  I should be able to navigate to any site

  Scenario: Verify user is able to submit his contact data
    Given I navigate to home page
    When I select contact us from menu
    Then I should see submit form
#    When I enter details and submit
#    Then I should see details are submitted successfully