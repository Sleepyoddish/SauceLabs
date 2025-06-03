from config import BASE_URL
from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def verify_login_header(self):
        assert self.page.locator(".login_logo").is_visible()

    def verify_usernames_list(self):
        username_box = self.page.locator(".login_credentials")
        assert username_box.get_by_role("heading", name="Accepted usernames are:").is_visible()
        accepted_usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
        for username in accepted_usernames:
            assert username_box.get_by_text(username).is_visible(), f"Username not found: {username}"

    def verify_passwords_list(self):
        password_box = self.page.locator(".login_password")
        assert password_box.get_by_role("heading", name= "Password for all users:").is_visible()
        assert password_box.get_by_text("secret_sauce").is_visible()

    def verify_login_username_errors(self):

        login_errors = [
            ("locked_out_user", "Epic sadface: Sorry, this user has been locked out."),
            ("problem_user", "Epic sadface: Unexpected issue with the login."),
            ("invalid_user", "Epic sadface: Username and password do not match any user."),
        ]

        for username, expected_error in login_errors:
            self.page.fill("#user-name", username)
            self.page.fill("#password", "secret_sauce")
            self.page.click("#login-button")

            error_text = self.page.locator("[data-test='error']").text_content().strip()
            assert error_text == expected_error, f"For {username}, expected: '{expected_error}', but got: '{error_text}'"

            self.page.reload()