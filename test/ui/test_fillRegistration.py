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

def test_fill_registration_form(setup_browser):
    page = setup_browser
    page.goto(URLS["automation_testing_register"])

    page.wait_for_selector('//input[@placeholder="First Name"]').type('Kareem')
    page.wait_for_selector('//input[@placeholder="Last Name"]').type('Rahaf')
    page.query_selector('//textarea[@ng-model="Adress"]').type("123 Main Street")
    page.query_selector('//input[@ng-model="EmailAdress"]').type("rahaf@gmail.com")
    page.query_selector('//input[@value="Cricket"]').click()
    page.query_selector('//input[@ng-model="Phone"]').type("0598754111")

    page.select_option('//select[@id="country"]', 'India')
    page.select_option('//select[@id="yearbox"]', '2002')
    page.select_option('//select[@ng-model="monthbox"]', 'January')
    page.select_option('//select[@id="daybox"]', '8')

    page.wait_for_selector('//div[@id="msdd"]').click()
    page.wait_for_selector('//a[text()="Arabic"]').click()

    page.query_selector('//input[@id="firstpassword"]').type("123456")
    page.query_selector('//input[@id="secondpassword"]').type("123456")

    gender_radio = page.query_selector('//input[@value="Male"]')
    gender_radio.click()
    assert gender_radio.is_checked(), "Gender selection failed"

    skill_dropdown = page.query_selector('//select[@id="Skills"]')
    skill_dropdown.select_option(label='Art Design')
    page.wait_for_timeout(5000)
