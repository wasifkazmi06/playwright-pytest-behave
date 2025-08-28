from playwright.sync_api import Page
from pages.BasePage import BasePage
from pages.UserDashboardPage import UserDashboardPage


class LazypayHomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.main_heading = page.get_by_role("heading", name="India's Credit Super-App")
        self.login_button = page.get_by_role("button", name="Signup/Login")
        self.mobile_number_input = page.get_by_test_id("mobile-input-field")
        self.proceed_button = page.get_by_role("button", name="Proceed")
        self.title = page.title()
        self.otp_input_1 = page.get_by_label("OTP digit 1")
        self.otp_input_2 = page.get_by_label("OTP digit 2")
        self.otp_input_3 = page.get_by_label("OTP digit 3")
        self.otp_input_4 = page.get_by_label("OTP digit 4")
        self.otp_input_5 = page.get_by_label("OTP digit 5")
        self.otp_input_6 = page.get_by_label("OTP digit 6")
        self.confirm_button = page.get_by_test_id("confirm-otp")

    def click_login_button(self):
        self.login_button.click()

    def input_mobile_number(self, mobile):
        self.mobile_number_input.fill(mobile)

    def click_proceed_button(self):
        self.proceed_button.click()

    def input_otp(self, otp):
        self.otp_input_1.fill(otp[0])
        self.otp_input_2.fill(otp[1])
        self.otp_input_3.fill(otp[2])
        self.otp_input_4.fill(otp[3])
        self.otp_input_5.fill(otp[4])
        self.otp_input_6.fill(otp[5])

    def click_confirm_button(self):
        self.confirm_button.click()

    def return_user_dashboard(self):
        return UserDashboardPage(self.page)
