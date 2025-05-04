class ForgotPasswordPage:
    def __init__(self, page_handler):
        self.page_handler = page_handler
        self.locators = {
            "forgot_link": '//p[text()="Forgot your password? "]',
            "reset_header": "h6:has-text('Reset Password')",
            "username_field": 'input[name="username"]',
            "reset_button": 'button[type="submit"]',
            "reset_confirmation": "h6:has-text('Reset Password link sent successfully')"
        }

    def click_forgot_password_link(self):
        self.page_handler.wait_for_selector(self.locators["forgot_link"]).click()

    def verify_reset_header(self):
        reset_header = self.page_handler.wait_for_selector(self.locators["reset_header"], timeout=5000)
        assert reset_header.is_visible(), "'Reset Password' header not visible as expected"

    def enter_username(self, username):
        self.page_handler.fill(self.locators["username_field"], username)

    def click_reset_button(self):
        self.page_handler.click(self.locators["reset_button"])

    def verify_reset_confirmation(self):
        confirmation_message = self.page_handler.wait_for_selector(self.locators["reset_confirmation"], timeout=5000)
        assert confirmation_message.is_visible(), "Reset confirmation not visible"
