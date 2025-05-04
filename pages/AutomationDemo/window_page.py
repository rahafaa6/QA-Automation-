class WindowPage:
    def __init__(self, page_handler, urls):
        self.page_handler = page_handler
        self.urls = urls
        self.locators = {
            "click_new_window": '//button[contains(text()," click ")]'
        }

    def navigate_to_page(self):
        self.page_handler.goto(self.urls["automation_testing_windows"])

    def click_new_window(self):
        button = self.page_handler.wait_for_selector(self.locators["click_new_window"])
        button.click()

    def get_open_pages(self):
        return self.page_handler.context.pages

    def print_page_titles(self, pages):
        print(f"Number of open pages: {len(pages)}")
        for i, p in enumerate(pages):
            print(f"Page {i} URL: {p.url}")
        print("Original page title:", self.page_handler.title())

    def switch_and_close_new_page(self, pages):
        if len(pages) > 1:
            new_page = pages[1]
            new_page.bring_to_front()
            self.page_handler.wait_for_timeout(3000)
            print("New page title:", new_page.title())
            new_page.close()
        else:
            print("No new page was opened.")