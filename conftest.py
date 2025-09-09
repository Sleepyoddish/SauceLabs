import os
import pytest
from playwright.sync_api import sync_playwright

# ==================== HEADLESS & SLOWMO SETTINGS ====================
# Default: run headed locally, headless in CI
CI = os.getenv("CI", "false").lower() == "true"
HEADLESS = CI  # True if running in CI, False if local
SLOWMO = int(os.getenv("SLOWMO", "300"))

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    print(f"Launching browser with headless={HEADLESS}, slow_mo={SLOWMO}")
    browser = playwright_instance.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOWMO
    )
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

