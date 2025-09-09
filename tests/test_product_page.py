import pytest

from data.product_page_data import swag_labs_header
from pages.base_page import BasePage
from pages.product_page import ProductPage


# ============================ PRODUCT PAGE HEADER TEST============================
#This test verifies the header on the product page of the app
@pytest.mark.product
def test_product_page_header(page):
    login = BasePage(page)
    product = ProductPage(page)
    login.login()
    product.verify_header(swag_labs_header)

# ============================ PRODUCT PAGE PRODUCT LIST TEST============================
#This test verifies the number and names of products on the product page
@pytest.mark.product
def test_product_list(page):
    login = BasePage(page)
    product = ProductPage(page)
    login.login()
    product.verify_product_names()