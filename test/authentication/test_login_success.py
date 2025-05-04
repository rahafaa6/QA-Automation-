import pytest
from ..urls import URLS

LOGIN_LOCATORS = {
    "username": "input[name='username']",
    "password": "input[type='password']",
    "submit_button": "button[type='submit']",
    "dashboard_header": "h6:has-text('Dashboard')",
}

@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),  # Valid credentials
])
def test_login_success(page_handler, username, password):
    page_handler.goto(URLS["orangehrm"])

    # Fill in the login form
    page_handler.locator(LOGIN_LOCATORS["username"]).fill(username)
    page_handler.locator(LOGIN_LOCATORS["password"]).fill(password)
    page_handler.locator(LOGIN_LOCATORS["submit_button"]).click()

    # Wait for the dashboard header to ensure login was successful
    page_handler.wait_for_selector(LOGIN_LOCATORS["dashboard_header"], timeout=10000)
    # Assert that the URL has changed (indicating successful login)
    assert page_handler.url != URLS["orangehrm"], f"Login failed. Current URL: {page_handler.url}"
