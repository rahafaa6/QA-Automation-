from playwright.sync_api import sync_playwright

def handle_rejex (response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url :
        status = response.status
        data = response.text()
        print(f'status: {status} \ndata: {data}')

with sync_playwright() as p:
    broswer = p. chromium. launch()
    context = broswer.new_context()
    page = context.new_page ()
    page. goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php#google_vignette')

    # <select name="cat" onchange="AjaxFunction();" id="s1">
    select = page.wait_for_selector('//select[@id="s1"]')

    page.on('response', lambda response : handle_rejex(response))
    # «option value="2">Colors</option>
    select.select_option('2')
    page.wait_for_timeout(555555555)