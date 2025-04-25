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

def test_forgot_password_flow(page):
    page.goto(URLS['orangehrm'])
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    reset_header = page.wait_for_selector("h6:has-text('Reset Password')", timeout=5000)
    assert reset_header.is_visible(), "'Reset Password' header not visible as expected"

    page.wait_for_timeout(3000)
