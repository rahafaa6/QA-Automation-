import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page_handler():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
