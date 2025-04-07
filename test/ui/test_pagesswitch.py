from playwright.sync_api import sync_playwright


def wait_for_timeout():
    pass


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')

    #<button class="btn btn-info">    click   </button>
    page.wait_for_selector('//button[contains(text()," click ")]').click()
    page.wait_for_timeout(3000)
    # How to find the total pages
    total_pages = context.pages
    #print number of page that open
    print(len(total_pages))
    #print (the url of the title)
    for i in total_pages:
        print(i)

    print(page.title())
    new_page = total_pages[1]
    #How to switch to new page
    new_page.bring_to_front()
    page.wait_for_timeout(3000)
    print(new_page.title())
    new_page.close()
    wait_for_timeout()
    browser.close()