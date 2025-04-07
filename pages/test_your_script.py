from playwright.sync_api import sync_playwright

with sync_playwright() as Locators:
    browser = Locators.chromium.launch(headless=False)
    page = browser.new_page()
    page. goto ('https://demo.automationtesting.in/Register.html')

    username_element = page.wait_for_selector('//input[@placeholder="First Name"]')
    username_element. type('Kareem')

    page.wait_for_selector('//input[@placeholder="Last Name"]').type('Rahaf')
    page.query_selector('//textarea[@ng-model="Adress"]').type("123 Main Street")
    #page.query_selector('//input[@value="Male"]').click()
    page.query_selector('//input[@ng-model="EmailAdress"]').type("rahaf@gmail.com")
    page.query_selector('//input[@value="Cricket"]').click()
    page.query_selector('//input[@ng-model="Phone"]').type("0598754111")
    page.select_option('//select[@id="country"]', 'India')
    page.select_option('//select[@id="yearbox"]', '2002')
    page.select_option('//select[@ng-model="monthbox"]','January')
    page.select_option('//select[@id="daybox"]', '8')
    page.wait_for_selector('//div[@id="msdd"]').click()
    page.wait_for_selector('//a[text()="Arabic"]').click()
    page.query_selector('//input[@id="firstpassword"]').type("123456")
    page.query_selector('//input[@id="secondpassword"]').type("123456")

    butt=page.query_selector('//input[@value="Male"]')
    butt.click()
    if butt.is_checked():
        print("passed")
    else:
        print("failed")

    # Select Drop
    # 1. Find the select Location
    select_dropdown = page.query_selector('//select[@id="Skills"]')
    # 2. Select the option
    select_dropdown.select_option(label='Art Design')
    page.wait_for_timeout (5000000)



