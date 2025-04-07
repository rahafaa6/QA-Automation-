from playwright.sync_api import sync_playwright

with sync_playwright() as Locators:
    browser = Locators.chromium.launch(headless=False)
    page = browser.new_page()
    page. goto ('https://demo.automationtesting.in/Register.html')

    username_element = page.wait_for_selector('//input[@placeholder="First Name"]')
    username_element. type('Kareem')

    page.wait_for_selector('//input[@placeholder="Last Name"]').type('Rahaf')
    page.query_selector('//textarea[@ng-model="Adress"]').type("123 Main Street")


    # Select Drop
    # 1. Find the select Location
    select_dropdown = page.query_selector('//select[@id="Skills"]')
    # 2. Select the option
    select_dropdown.select_option(label='Art Design')
    page.wait_for_timeout (5000000)