import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="class")
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.mark.usefixtures("browser")
class TestTitleClass:
    def test_goto_google(self, page):
        page.goto(URLS["google"])
        assert page.url == URLS["google"]

    def test_orange(self, page):
        page.goto(URLS["orangehrm"])
        assert page.url == URLS["orangehrm"]

    def test_orange1(self, page):
        page.goto(URLS["orangehrm"])
        assert page.url == URLS["orangehrm"]
