import os
from playwright.sync_api import Page

class FileUploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input_locator = "input#input-4"
        self.file_name_display_locator = "span#input-4-filename"

    def set_file_input(self, file_path: str):
        self.page.set_input_files(self.file_input_locator, file_path)

    def get_uploaded_file_name(self) -> str:
        self.page.wait_for_selector(self.file_name_display_locator, timeout=5000)
        return self.page.locator(self.file_name_display_locator).text_content().strip()

    def navigate_to_page(self, url: str):
        self.page.goto(url)

def get_file_path():
    file_path = os.path.abspath(os.path.join("uploads", "test.txt"))

    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Sample content for the file upload")

    return file_path
