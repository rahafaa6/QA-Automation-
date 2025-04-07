import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page_handler(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.mark.parametrize("invalid_username,invalid_password", [('admin', 'admin'),('hdnj', 'djud')])
def test_login_page(page_handler, invalid_username, invalid_password):
    page_handler.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page_handler.wait_for_selector('//input[@name="username"]')
    page_handler.fill('//input[@name="username"]', invalid_username)
    page_handler.fill('//input[@name="password"]', invalid_password)
    page_handler.click('//button[@type="submit"]')
    page_handler.wait_for_timeout(3000)
    error_message = page_handler.wait_for_selector('//p[contains(@class, "oxd-text")]').text_content().strip()
    assert error_message == "Invalid credentials"
