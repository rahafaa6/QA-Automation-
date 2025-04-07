from playwright.sync_api import sync_playwright

with sync_playwright() as Locators:
    browser = Locators.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    page = browser.new_page()

    # Video Directory
    context = browser.new_context(record_video_dir='./videos') 
    page = context.new_page()

    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # <input class="oxd-input oxd-input—-active" name="username" placeholder="Username" autofocus data-v-1f99f73c>
    # page.wait_for_selector('//input[@name="username"] '). fill('Admin')
    page.wait_for_selector('//input[@name="username"]')
    page.query_selector('//input[@name="username"]').fill('Admin')

    # «input class="oxd-input oxd-input--active" type="password" name="password" placeholder="Password">
    # page wait_for_selector(*//input [@name="password"] '). fill('admin123')
    page.wait_for_selector('//input[@name="username"]')
    page.query_selector(' // input[ @ name = "password"]'). fill('admin123')

    #take screenshot
    page.screenshot(path='./screenshots/loginpage.png')
    page.query_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.screenshot(path='./screenshots/homepage.png')
    page.wait_for_timeout(3000)
    context.close()

