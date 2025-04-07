from playwright.sync_api import sync_playwright

"""""
    with sync_playwright() as p:
        broswer = p.chromium. launch(headless=False)
        context = broswer.new_context()
        page = context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')
    
        # Store multiple elements using list
        # <b>Sakinalium - Readability</b>
        elements = page.query_selector_all('b')
        print(len(elements))
        for i in elements:
            print(i.text_content())
    
        # <a href="http://www.automationtesting.in" class="navbar-brand">
        elements = page.query_selector_all('a')
        print(len(elements))
        for i in elements:
            print(i.get_attribute('href'))
        page.wait_for_timeout(5000)
"""""

with sync_playwright() as p:
    try:
        broswer = p.chromium.launch(headless=False)
        context = broswer.new_context()
        page = context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')

        #wronge sellector
        #page.query_selector('d//[@sf="werf"]').click()
        # will print Execute
        
        # <a href="http://www.automationtesting.in" class="navbar-brand">
        elements = page.query_selector_all('a')
        print(len(elements))
        for i in elements:
            print(i.get_attribute('href'))
        page.wait_for_timeout(5000)
    except Exception as e :
        print(str(e))
    finally:
        print('Execute')