import pytest

from config import BASE_URL
from pages.login_page import LoginPage

# ============================ LOGIN PAGE HEADER TEST============================
def test_login_page_header(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login_header()

def test_login_page_usernames(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.usernames_list()

def test_login_page_passwords(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.passwords_list()

