Feature: Login
  Login to the Lazypay website dashboard

  Scenario Outline: Login to Lazypay website as a user
    Given I navigate to Lazypay website
    Then I validate that correct website is opened
    When I click on Signup/Login button
    And I enter my mobile number as "<mobile_number>"
    And I click on the proceed button
    And I enter the OTP for "<mobile_number>"
    And I click on the Confirm button
    Then I validate that user has logged in successfully

    Examples:
    | mobile_number|
    |6000000120    |
