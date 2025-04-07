from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page. goto ('https://www.redbus.in/')

    # Gives all the cookies
    my_cookies = page.context.cookies()
    print(my_cookies)
    # Clear the all the cookies
    page.context.clear_cookies()
    new_cookies = {
    ' name' : 'ravi' ,
    'udid': '4375y34975y3947595483'
    }
    # To pass the new cookies to the rage
    # Rage.context.add_cookies([new_cookies])
    
    # Taking screenshot
    page.screenshot(path='../screenshots/test.png', full_page=True)