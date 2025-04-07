from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    contect = browser.new_context()
    page = contect.new_page ()
    page. goto ('https://demo.automationtesting.in/FileUpload.html')

    file_upload = './test.txt'

    # «input id="input-4" name="input4[]" type="file" multiple class>
    upload_location = page.query_selector('//input[@id="input-4"]')

    #To Upload the file
    upload_location.set_input_files(file_upload)
    page. wait_for_timeout (3000)