from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    broswer = p.chromium. launch(headless=False)
    context = broswer.new_context()
    page = context.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')

    # <table id="customers" style="border-collapse: collapse;box-sizing: inherit;color:#000; font-size:15px;width: 677.156px">
    table = page.wait_for_selector('//table[@id="customers"]')

    # <tr style="box-sizing: inherit">@</tr›
    tr = table.query_selector_all('tr')
    print(len(tr))

    # <td style="border: 1px solid #ddd;box-sizing: inherit;padding:8px">
    td = table.query_selector_all('td')
    print(len(td))

    for row in tr:
        cells = row.query_selector_all('td')
        for cell in cells:
         print(cell.text_content())
    page.wait_for_timeout(2000)





