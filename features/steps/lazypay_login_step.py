from behave import *
from playwright.sync_api import sync_playwright
from pages.LazypayHomePage import LazypayHomePage


@given("I navigate to Lazypay homepage")
def go_to_lazypay_website(context):
    print(u'Step: Given I navigate to google website')
    context.page = context.browser.new_page()
    context.home_page = LazypayHomePage(context.page)
    context.home_page.go_to("https://sandbox-web.lazypay.in/")


@when("I validate the page title")
def validate_title(context):
    title = context.home_page.title()
    print(title)
    assert title == "Apply for Instant Personal Loan and Buy now Pay Later with LazyPay"


@then("I click on Signup/Login button")
def click_on_login_button(context):
    context.home_page. home_page.login_button.click()


@then("I enter my mobile number")
def input_mobile_number(context):
    context.page.mobile_number_input.fill("7057031852")


@then("I click on the proceed button")
def click_on_proceed_button(context):
    context.page.proceed_button.click()


@then("I enter the OTP")
def input_otp(context):
    print(u'Step: Then I click on the search button')


@then("I click on the Confirm button")
def click_on_confirm_button(context):
    print(u'Step: Then I click on the search button')