from pages.OrangeHRM.forgot_password_page import ForgotPasswordPage
from ..urls import URLS

def test_forgot_password_flow(page_handler):
    forgot_password_page = ForgotPasswordPage(page_handler)
    page_handler.goto(URLS['orangehrm'])
    forgot_password_page.click_forgot_password_link()
    forgot_password_page.verify_reset_header()
    forgot_password_page.enter_username('Admin')
    forgot_password_page.click_reset_button()
    forgot_password_page.verify_reset_confirmation()
