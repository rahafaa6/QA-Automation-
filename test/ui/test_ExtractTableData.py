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

def test_extract_table_data(setup_browser):
    page = setup_browser
    page.goto(URLS["techlistic_table"])
    table = page.wait_for_selector('//table[@id="customers"]')
    rows = table.query_selector_all('tr')
    assert len(rows) > 0, "The table does not contain rows."
    cells = table.query_selector_all('td')
    assert len(cells) > 0, "The table does not contain cells."
    for row in rows:
        cells = row.query_selector_all('td')
        for cell in cells:
            print(cell.text_content().strip())
    assert len(rows) > 0, "No rows were extracted from the table."
