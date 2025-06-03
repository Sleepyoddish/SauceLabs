from playwright.sync_api import Page

from config import BASE_URL, USERNAME, PASSWORD


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self):
        self.page.goto(BASE_URL)

    def login(self):
        self.page.go_to(BASE_URL)
        self.page.get_by_placeholder("Username").fill(USERNAME)
        self.page.get_by_placeholder("Password").fill(PASSWORD)
        self.page.get_by_role("button", name="login-button")