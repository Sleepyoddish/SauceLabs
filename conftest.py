import os

import pytest
from playwright.sync_api import sync_playwright

# ==================== HEADLESS & SLOWMO SETTINGS ====================
HEADLESS = os.getenv("HEADLESS", "false").lower() != "false"
SLOWMO = int(os.getenv("SLOWMO", "300"))

# ==================== PLAYWRIGHT FIXTURES ====================
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    print(f"Launching browser with headless={HEADLESS}, slow_mo={SLOWMO}")
    browser = playwright_instance.chromium.launch(headless=HEADLESS, slow_mo=SLOWMO)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 800})
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()