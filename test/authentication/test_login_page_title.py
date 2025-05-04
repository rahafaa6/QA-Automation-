from ..urls import URLS

def test_login_page_title(page_handler):
    page_handler.goto(URLS["orangehrm"])
    assert page_handler.title() == 'OrangeHRM', "Page title does not match"
