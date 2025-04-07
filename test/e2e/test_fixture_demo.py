import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="module")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_goto_google(page):
    page.goto('https://www.google.com/')
    page.wait_for_timeout(2000)
    assert 'Google'== page.title()

def test_goto_rudbus(page):
    page.goto('https://www.redbus.in/')
    page.wait_for_timeout(2000)
    assert 'redBus' in page.title()

