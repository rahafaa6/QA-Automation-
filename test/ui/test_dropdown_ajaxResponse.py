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

def test_dropdown_ajax_response(setup_browser):
    def handle_response(response):
        if URLS["ajax_response"] in response.url:
            status = response.status
            try:
                data = response.text()
            except:
                data = "[Failed to get text content]"
            print(f"Status: {status}\nData: {data}\nURL: {response.url}")

    page = setup_browser
    page.on('response', handle_response)
    page.goto(URLS["ajax_dropdown"])
    select = page.wait_for_selector('//select[@id="s1"]')
    select.select_option('2')
    page.wait_for_timeout(5000)
