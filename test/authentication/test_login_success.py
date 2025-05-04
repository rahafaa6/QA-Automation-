from pages.OrangeHRM.LoginPage import LoginSuccess
from ..urls import URLS

def test_login_success(page_handler):
    login_success = LoginSuccess(page_handler)
    page_handler.goto(URLS["orangehrm"])
    login_success.enter_credentials("Admin", "admin123")
    login_success.submit_form()
    assert login_success.verify_dashboard(), "Login failed or dashboard not displayed."
