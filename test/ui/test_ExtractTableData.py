from pages.AutomationDemo.table_page import TablePage
from ..urls import URLS

def test_extract_table_data(page_handler):
    table_page = TablePage(page_handler, URLS)
    table_page.navigate_to_table_page()
    table = table_page.get_table()
    rows = table_page.extract_rows(table)
    cells = table_page.extract_cells(table)
    table_page.verify_table(rows, cells)
    table_page.print_table_data(rows)
    assert len(rows) > 0, "No rows were extracted from the table."