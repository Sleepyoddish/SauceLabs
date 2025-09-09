from config import BASE_URL
from data.product_page_data import products
from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def verify_header(self, locator):
        self.page.wait_for_timeout(2000)
        assert self.page.locator(locator).is_visible()

    def verify_product_names(self):
        product_count = self.page.locator(".inventory_item_name").count()
        for i in range(product_count):
            for product in products:
                assert self.page.locator(".inventory_item_name", has_text= product).is_visible(), f"Expected: {products}, but got: {self.page.locator(".inventory_item_name").all_text_contents()}"