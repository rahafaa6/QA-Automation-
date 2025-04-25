import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_login_page_title(page):
    page.goto(URLS["orangehrm"])
    assert page.title() == 'OrangeHRM', "Page title does not match"
