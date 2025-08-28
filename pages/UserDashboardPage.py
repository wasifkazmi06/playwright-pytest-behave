from playwright.sync_api import Page
from pages.BasePage import BasePage


class UserDashboardPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.due_amount_tag = page.get_by_role("heading", name="Due amount")

    def validate_successful_login(self, mobile):
        pass
