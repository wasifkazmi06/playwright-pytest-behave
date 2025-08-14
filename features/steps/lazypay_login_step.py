from behave import *
from playwright.sync_api import expect
from pages.LazypayHomePage import LazypayHomePage
from utilities import GetOTP, ConfigReader


@given("I navigate to Lazypay homepage")
def go_to_lazypay_website(context):
    print(u'Step: Given I navigate to google website')
    context.lazypay_home_page = LazypayHomePage(context.page)
    context.lazypay_home_page.go_to(ConfigReader.read_config("url", "lazypay_website_url"))


@then("I validate that correct website is opened")
def validate_title(context):
    title = context.lazypay_home_page
    print(f"Title: {title}")
    # assert title == "Apply for Instant Personal Loan and Buy now Pay Later with LazyPay"


@when("I click on Signup/Login button")
def click_on_login_button(context):
    context.lazypay_home_page.click_login_button()


@when(u'I enter my mobile number as "{mobile_number}"')
def input_mobile_number(context, mobile_number):
    context.lazypay_home_page.input_mobile_number(mobile_number)


@when("I click on the proceed button")
def click_on_proceed_button(context):
    context.lazypay_home_page.click_proceed_button()


@when(u'I enter the OTP for "{mobile_number}"')
def input_otp(context, mobile_number):
    otp = str(GetOTP.GetOTP.get_otp(context, mobile_number, ConfigReader.read_config("secret", "tenant_id")))
    print(f"OTP is: {otp}")
    context.lazypay_home_page.input_otp(otp)


@when("I click on the Confirm button")
def click_on_confirm_button(context):
    context.lazypay_home_page.click_confirm_button()


@then("I validate that user has logged in successfully")
def validate_login_session(context):
    expect(context.lazypay_home_page.return_user_dashboard().due_amount_tag).to_be_visible()
