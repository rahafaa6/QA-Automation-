import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_register_demo_website(page):
    page.goto(URLS['automation_testing_register'])

    page.wait_for_selector('//input[@placeholder="First Name"]').type('Kareem')
    page.wait_for_selector('//input[@placeholder="Last Name"]').type('Rahaf')
    page.wait_for_selector('//textarea[@ng-model="Adress"]').type("123 Main Street")
    page.wait_for_selector('//input[@ng-model="EmailAdress"]').type("rahaf@gmail.com")
    page.wait_for_selector('//input[@ng-model="Phone"]').type("0598754111")

    gender = page.wait_for_selector('//input[@value="Male"]')
    gender.click()

    cricket = page.wait_for_selector('//input[@value="Cricket"]')
    cricket.click()

    page.select_option('//select[@id="country"]', 'India')
    page.select_option('//select[@id="yearbox"]', '2002')
    page.select_option('//select[@ng-model="monthbox"]', 'January')
    page.select_option('//select[@id="daybox"]', '8')

    page.wait_for_selector('//div[@id="msdd"]').click()
    page.wait_for_selector('//a[text()="Arabic"]').click()

    page.select_option('//select[@id="Skills"]', label='iOS')

    page.wait_for_selector('//input[@id="firstpassword"]').type("123456")
    page.wait_for_selector('//input[@id="secondpassword"]').type("123456")

    assert gender.is_checked(), "Gender was not selected"

    submit_button = page.wait_for_selector('button[type="submit"]')
    submit_button.click()

    page.wait_for_timeout(5000)
