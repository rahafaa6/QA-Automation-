from playwright.sync_api import sync_playwright

text_alert = []

def handle_dialog(dialog):
    message = dialog.message
    text_alert. append (message)
    dialog.accept()

with sync_playwright() as Locators:
    browser = Locators.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')


    #page.wait_for_selector('//div[@id="0KTab"]/button').click()

    #<a href="#CancelTab" data-toggle="tab" class="analystic" aria-expanded="true">Alert with OK &amp; Cancel </a>
    page.wait_for_selector('//a[@href="#CancelTab"]').click() #to select Alert with OK & Cancel
    page.wait_for_timeout (2000)

    # control alert
    #page.on("dialog", lambda dialog: dialog.accept())
    #page.on("dialog", lambda dialog: dialog.dismiss())
    #page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", handle_dialog)

    # <div id="CancelTab" class="tab-pane col-md-6 col-nd-offset-1 col-xs-4 col-s-offset-1 active">
    page.wait_for_selector('//div[@id="CancelTab"]/button').click() # to select and click the button to display a confirmation box
    page.wait_for_timeout (5000000)
    print(text_alert[0])