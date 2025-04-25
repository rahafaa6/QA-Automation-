import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page, context
        browser.close()

def test_open_multiple_windows_demo(setup_browser):
    page, context = setup_browser
    page.goto(URLS["automation_testing_windows"])

    # Click to open a new window
    page.wait_for_selector('//button[contains(text()," click ")]').click()

    page.wait_for_timeout(3000)

    total_pages = context.pages
    print(f"Number of open pages: {len(total_pages)}")

    for i, p in enumerate(total_pages):
        print(f"Page {i} URL: {p.url}")

    print("Original page title:", page.title())

    if len(total_pages) > 1:
        new_page = total_pages[1]
        new_page.bring_to_front()
        page.wait_for_timeout(3000)
        print("New page title:", new_page.title())
        new_page.close()
    else:
        print("No new page was opened.")
