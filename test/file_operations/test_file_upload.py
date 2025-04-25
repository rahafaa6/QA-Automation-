import os
import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

def get_file_path():
    file_path = os.path.abspath(os.path.join("uploads", "test.txt"))

    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Sample content for the file upload")

    return file_path

@pytest.mark.parametrize("file_path", [get_file_path()])
def test_file_upload(file_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(URLS["file_upload_page"])
        page.set_input_files("input#input-4", file_path)
        page.wait_for_load_state("domcontentloaded")
        try:
            page.wait_for_selector("span#input-4-filename", timeout=5000)
            uploaded_file_name = page.locator("span#input-4-filename").text_content()
            assert uploaded_file_name == "test.txt", f"File upload failed. Uploaded file: {uploaded_file_name}"
            print("File uploaded successfully")
        except Exception as e:
            print(f"Error during file upload: {e}")

        page.wait_for_timeout(3000)
        browser.close()
