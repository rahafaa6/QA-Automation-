from pages.Other.redbus_page import RedbusPage
from ..urls import URLS

def test_redbus_operations(page_handler):
    redbus = RedbusPage(page_handler, URLS)
    redbus.open_redbus()
    redbus.print_and_clear_cookies()
    redbus.add_custom_cookie()
    redbus.capture_screenshot()
