import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def browser_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page, context
        browser.close()

def visit_redbus(page):
    page.goto(URLS["redbus"])
    page.wait_for_timeout(3000)

def handle_cookies(context):
    cookies = context.cookies()
    print("Original cookies:", cookies)

    context.clear_cookies()
    print("Cookies cleared.")

    context.add_cookies([{
        'name': 'ravi',
        'value': '4375y34975y3947595483',
        'domain': 'redbus.in',
        'path': '/',
    }])
    print("New cookie added.")

def take_screenshot(page):
    page.screenshot(path='screenshots/test.png', full_page=True)
    print("Screenshot saved.")

@pytest.mark.parametrize('url', [URLS["redbus"]])
def test_redbus_operations(browser_setup, url):
    page, context = browser_setup
    visit_redbus(page)
    handle_cookies(context)
    take_screenshot(page)
