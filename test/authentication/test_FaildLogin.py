import pytest
from pages.OrangeHRM.LoginPage import FailedLogin
from ..urls import URLS

@pytest.mark.parametrize("invalid_username, invalid_password", [
    ('admin', 'admin'),
    ('hdnj', 'djud')
])
def test_login_page_invalid_credentials(page_handler, invalid_username, invalid_password):
    login_page = FailedLogin(page_handler)
    page_handler.goto(URLS["orangehrm"])

    login_page.enter_credentials(invalid_username, invalid_password)
    login_page.submit_form()

    error_element = login_page.get_error_message()
    assert error_element.is_visible(), "Error message not displayed as expected"