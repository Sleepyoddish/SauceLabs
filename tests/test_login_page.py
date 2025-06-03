import pytest

from config import BASE_URL
from pages.login_page import LoginPage

# ============================ LOGIN PAGE HEADER TEST============================
def test_login_page_header(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_login_header()

def test_login_page_usernames(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_usernames_list()

def test_login_page_passwords(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_passwords_list()

def test_login_page_errors(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.verify_login_username_errors()