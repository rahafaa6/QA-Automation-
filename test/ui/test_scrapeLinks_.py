import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page, context, browser
        browser.close()

def test_scrape_links_from_page(setup_browser):
    page, context, browser = setup_browser
    try:
        page.goto(URLS["automation_testing_selectable"])
        elements = page.query_selector_all('a')
        print(f"Number of <a> tags: {len(elements)}")
        for i in elements:
            href = i.get_attribute('href')
            if href:
                print(href)

        page.wait_for_timeout(5000)

    except Exception as e:
        pytest.fail(f"Error: {str(e)}")
    finally:
        if context:
            context.close()
        if browser:
            browser.close()
        print('Execute')
