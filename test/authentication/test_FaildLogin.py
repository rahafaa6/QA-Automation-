import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page_handler(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.mark.parametrize("invalid_username, invalid_password", [
    ('admin', 'admin'),
    ('hdnj', 'djud')
])
def test_login_page_invalid_credentials(page_handler, invalid_username, invalid_password):
    page_handler.goto(URLS["orangehrm"])

    page_handler.fill('//input[@name="username"]', invalid_username)
    page_handler.fill('//input[@name="password"]', invalid_password)
    page_handler.click('//button[@type="submit"]')

    error_element = page_handler.wait_for_selector('//p[text()="Invalid credentials"]', timeout=10000)
    error_message = error_element.text_content().strip()

    assert error_message == "Invalid credentials"