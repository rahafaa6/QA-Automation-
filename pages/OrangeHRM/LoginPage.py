class FailedLogin:
    def __init__(self, page_handler):
        self.page_handler = page_handler
        self.login_locators = {
            "username": '//input[@name="username"]',
            "password": '//input[@name="password"]',
            "submit_button": '//button[@type="submit"]',
            "error_message": '//p[text()="Invalid credentials"]',
            "dashboard_header": "h6:has-text('Dashboard')",
        }

    def enter_credentials(self, username, password):
        self.page_handler.fill(self.login_locators["username"], username)
        self.page_handler.fill(self.login_locators["password"], password)

    def submit_form(self):
        self.page_handler.click(self.login_locators["submit_button"])

    def get_error_message(self):
        return self.page_handler.wait_for_selector(self.login_locators["error_message"], timeout=10000)


class LoginSuccess:
    def __init__(self, page_handler):
        self.page_handler = page_handler
        self.login_locators = {
            "username": '//input[@name="username"]',
            "password": '//input[@name="password"]',
            "submit_button": '//button[@type="submit"]',
            "dashboard_header": 'h6:has-text("Dashboard")',
        }

    def enter_credentials(self, username, password):
        self.page_handler.fill(self.login_locators["username"], username)
        self.page_handler.fill(self.login_locators["password"], password)

    def submit_form(self):
        self.page_handler.click(self.login_locators["submit_button"])

    def verify_dashboard(self):
        dashboard_header = self.page_handler.wait_for_selector(self.login_locators["dashboard_header"], timeout=10000)
        return dashboard_header.is_visible()


class LoginPageWithMedia:
    def __init__(self, page_handler, urls):
        self.page_handler = page_handler
        self.urls = urls
        self.locators = {
            "username_input": '//input[@name="username"]',
            "password_input": '//input[@name="password"]',
            "submit_button": '//button[@type="submit"]',
        }

    def go_to_login_page(self):
        self.page_handler.goto(self.urls["orangehrm"])

    def perform_login(self, username, password):
        self.page_handler.wait_for_selector(self.locators["username_input"]).fill(username)
        self.page_handler.wait_for_selector(self.locators["password_input"]).fill(password)
        self.page_handler.screenshot(path='screenshots/login_page.png')
        self.page_handler.query_selector(self.locators["submit_button"]).click()
        self.page_handler.wait_for_timeout(3000)
        self.page_handler.screenshot(path='screenshots/homepage.png')

    def check_video_saved(self, video_path='reports/videos/login_video.mp4'):
        return os.path.exists(video_path)
