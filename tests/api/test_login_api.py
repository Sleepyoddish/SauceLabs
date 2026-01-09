import pytest
from playwright.sync_api import sync_playwright
from pages.api.login_api_page import LoginApiPage


# ============================ LOGIN API TEST============================
#This test verifies the login API
@pytest.mark.login
def test_login_api():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        login_api = LoginApiPage(page, p)

        response = login_api.login_api()
        print("Response:", response.status)

        login_api.close_request()