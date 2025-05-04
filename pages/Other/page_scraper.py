class PageScraper:
    def __init__(self, page_handler, urls):
        self.page_handler = page_handler
        self.urls = urls
        self.locators = {
            "all_links": 'a'
        }

    def scrape_all_links(self):
        self.page_handler.goto(self.urls["automation_testing_selectable"])
        elements = self.page_handler.query_selector_all(self.locators["all_links"])
        print(f"Number of <a> tags: {len(elements)}")

        links = []
        for element in elements:
            href = element.get_attribute('href')
            if href:
                links.append(href)
                print(href)
        return links