import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS
from pages.AutomationDemo.file_upload_page import FileUploadPage, get_file_path

@pytest.mark.parametrize("file_path", [get_file_path()])
def test_file_upload(file_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        file_upload_page = FileUploadPage(page)
        file_upload_page.navigate_to_page(URLS["file_upload_page"])
        file_upload_page.set_file_input(file_path)

        try:
            uploaded_file_name = file_upload_page.get_uploaded_file_name()
            assert uploaded_file_name == "test.txt", f"File upload failed. Uploaded file: {uploaded_file_name}"
            print("File uploaded successfully")

        except Exception as e:
            print(f"Error during file upload: {e}")
        browser.close()
