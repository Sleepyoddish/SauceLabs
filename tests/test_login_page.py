import pytest

from config import BASE_URL
from pages.login_page import LoginPage

# ============================ LOGIN PAGE HEADER TEST============================
#This test verifies the header on the login page of the app
@pytest.mark.login
def test_login_page_header(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_login_header()

# ============================ LOGIN PAGE USERNAMES TEST============================
#This test verifies the different usernames the user has access to on the login page
@pytest.mark.login
def test_login_page_usernames(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_usernames_list()

# ============================ LOGIN PAGE PASSWORDS TEST============================
#This test verifies the different passwords the user has access to on the login page
@pytest.mark.login
def test_login_page_passwords(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_passwords_list()

# ============================ LOGIN PAGE ERRORS TEST============================
#This test verifies the different errors the user can encounter with bad credentials when logging in
@pytest.mark.login
def test_login_page_errors(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_login_username_errors()