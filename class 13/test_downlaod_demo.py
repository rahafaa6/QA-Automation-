from playwright.sync_api import sync_playwright

def download_handle (download) :
    location_file = './files/test.zip'
    download.save_as(location_file)

with sync_playwright() as p:
    broswer = p.chromium.launch(headless=False)
    page = broswer.new_page()
    page.goto ('https://demo.imacros.net/Automate/Downloads')
    page.on( 'download', download_handle)
    page.wait_for_selector('//a[@href="/Content/Download.zip"]').click()
    page.wait_for_timeout (2000)