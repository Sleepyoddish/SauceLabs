from pages.base_page import BasePage

class LoginApiPage(BasePage):
    def __init__(self, page, playwright):
        super().__init__(page)
        # Create a new API request context for this page
        self.request = playwright.request.new_context(base_url="https://www.saucedemo.com/v1")

    def login_api(self, username="standard_user", password="secret_sauce"):
        response = self.request.post("/", form={
            "user-name": username,
            "password": password
        })

        assert response.status in [200, 302], f"Login failed: {response.status}"
        return response

    def close_request(self):
        self.request.dispose()