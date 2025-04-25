import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_mouse_keyboard_actions(setup_browser):
    page = setup_browser
    page.goto(URLS["automation_testing_selectable"])
    page.locator('//a[text()="SwitchTo"]').hover()
    page.locator('//a[text()="SwitchTo"]').click()
    page.locator('//a[text()="SwitchTo"]').dblclick()
    page.locator('//a[text()="SwitchTo"]').click(button="right")
    page.locator('//a[text()="SwitchTo"]').click(modifiers=["Shift"])
    page.locator('//a[text()="SwitchTo"]').press("A")
    page.locator('//a[text()="SwitchTo"]').press("$")
    page.wait_for_timeout(3000)
