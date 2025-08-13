from playwright.sync_api import Page
from pages.BasePage import BasePage


class LazypayHomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.login_button = page.find_by_role("button", name="Signup/Login")
        self.mobile_number_input = page.get_by_test_id("mobile-input-field")
        self.proceed_button = page.find_by_role("button", name="Proceed")

    async def login(self, mobile):
        self.login_button.click()
        self.mobile_number_input.fill(mobile)
        self.proceed_button.click()
