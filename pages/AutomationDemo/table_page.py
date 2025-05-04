class TablePage:
    def __init__(self, page_handler, urls):
        self.page_handler = page_handler
        self.urls = urls
        self.locators = {
            "table_customers": '//table[@id="customers"]',
            "table_rows": 'tr',
            "table_cells": 'td'
        }

    def navigate_to_table_page(self):
        self.page_handler.goto(self.urls["techlistic_table"])

    def get_table(self):
        return self.page_handler.wait_for_selector(self.locators["table_customers"])

    def extract_rows(self, table):
        return table.query_selector_all(self.locators["table_rows"])

    def extract_cells(self, table):
        return table.query_selector_all(self.locators["table_cells"])

    def print_table_data(self, rows):
        for row in rows:
            row_cells = row.query_selector_all(self.locators["table_cells"])
            for cell in row_cells:
                print(cell.text_content().strip())

    def verify_table(self, rows, cells):
        assert len(rows) > 0, "The table does not contain rows."
        assert len(cells) > 0, "The table does not contain cells."