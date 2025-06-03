from config import BASE_URL
from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login_header(self):
        assert self.page.locator(".login_logo").is_visible()

    def usernames_list(self):
        username_box = self.page.locator(".login_credentials")
        assert username_box.get_by_role("heading", name="Accepted usernames are:").is_visible()
        accepted_usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
        for username in accepted_usernames:
            assert username_box.get_by_text(username).is_visible(), f"Username not found: {username}"

    def passwords_list(self):
        password_box = self.page.locator(".login_password")
        assert password_box.get_by_role("heading", name= "Password for all users:").is_visible()
        assert password_box.get_by_text("secret_sauce").is_visible()