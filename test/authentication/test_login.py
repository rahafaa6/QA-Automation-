import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.mark.parametrize("username, password, should_login", [
    ("admin", "admin123", True),
    ("admin", "wrongpass", False),
    ("wronguser", "admin123", False),
])
def test_login(browser_context, username, password, should_login):
    page = browser_context

    page.goto(URLS["orangehrm"])

    page.locator("input[name='username']").fill(username)
    page.locator("input[type='password']").fill(password)
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(3000)

    if should_login:
        assert page.url != URLS["orangehrm"], "Login failed with valid credentials"
    else:
        error_element = page.locator("p:has-text('Invalid credentials')")
        assert error_element.is_visible(), "Expected error message not found"
