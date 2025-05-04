from pages.AutomationDemo.window_page import WindowPage
from ..urls import URLS

def test_open_multiple_windows_demo(page_handler):
    window_page = WindowPage(page_handler, URLS)
    window_page.navigate_to_page()
    window_page.click_new_window()
    pages = window_page.get_open_pages()
    window_page.print_page_titles(pages)
    window_page.switch_and_close_new_page(pages)
