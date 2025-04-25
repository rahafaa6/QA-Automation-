import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_open_google(page):
    page.goto(URLS["google"])
    page.wait_for_load_state('load')
    assert 'Google' in page.title()

def test_open_redbus(page):
    page.goto(URLS["redbus"])
    page.wait_for_load_state('load')
    assert 'redBus' in page.title()
