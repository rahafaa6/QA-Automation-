class RedbusPage:
    def __init__(self, page_handler, urls):
        self.page = page_handler
        self.context = page_handler.context
        self.urls = urls

    def open_redbus(self):
        self.page.goto(self.urls["redbus"])
        self.page.wait_for_timeout(3000)

    def print_and_clear_cookies(self):
        cookies = self.context.cookies()
        print("Original cookies:", cookies)
        self.context.clear_cookies()
        print("Cookies cleared.")

    def add_custom_cookie(self):
        self.context.add_cookies([{
            'name': 'ravi',
            'value': '4375y34975y3947595483',
            'domain': 'redbus.in',
            'path': '/',
        }])
        print("New cookie added.")

    def capture_screenshot(self, path='screenshots/test.png'):
        self.page.screenshot(path=path, full_page=True)
        print("Screenshot saved.")
