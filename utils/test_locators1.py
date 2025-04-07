from playwright.sync_api import sync_playwright

with sync_playwright() as Locators:
    browser = Locators.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Index.html')


    # id using
    """"
    emailtxtbox = page.wait_for_selector('#email?')
    emailtxtbox,type('test@gmail.com')

    buttonlogin = page.wait_for_selector('#enterimg')
    buttonlogin.click()
    page.wait_for_timeout(3000)
    """

    # cssSelector - id - #, class - ., attribute tagnamel attribute = "value"]

    username = page.wait_for_selector("input[name='username']")
    username.type("admin")

    password = page.wait_for_selector("input[type='password']")
    username.type("admin123")
    Loginbutton = page.wait_for_selector('button[type="submit"]')
    Loginbutton.click()
    page.wait_for_timeout(3000)
