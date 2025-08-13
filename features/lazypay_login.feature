Feature: Login
  Login to the Lazypay website dashboard
  Scenario: Login to Lazypay website as a user
    Given I navigate to Lazypay homepage
    When I validate the page title
    Then I click on Signup/Login button
    Then I enter my mobile number
    Then I click on the proceed button
    Then I enter the OTP
    Then I click on the Confirm button
