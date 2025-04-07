from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page. goto ('https://demo.automationtesting.in/Selectable.html')

    #<a href="SwitchTo.html" data-toggle="dropdown" class="dropdown-toggle" aria-expanded="true">SwitchTo</a>
    #page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    #page.wait_for_selector('//a[harf = "SwitchTo.html"]').hover()
    #page.wait_for_selector('//a[harf = "SwitchTo.html"]').click()

    # Mouse Actions
    # Hover the dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    # Click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
    # Double Click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    # Right on Element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button="right")
    # Shift Click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])

    # Keyboard
    page.wait_for_selector('//a[text()="SwitchTo"]').press("A")
    # A-Z, 0-9, F1-F12, All special character, ArrowRight, ArrowDown, PageUp, Enter, Control, Command page.wait_for_selector('//a[text()="SwitchTo"] ').press("$")
    page.wait_for_selector('//a[text()="SwitchTo"] ').press("$")


    page.wait_for_timeout(5000000)