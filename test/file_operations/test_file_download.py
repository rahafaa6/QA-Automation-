import os
import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

def download_file(page, download_folder):
    links = page.query_selector_all("a")
    target_file_name = None

    for link in links:
        text = link.text_content().strip()
        if text.endswith((".txt", ".json", ".jpg", ".png")):
            target_file_name = text
            break

    if target_file_name:
        with page.expect_download() as download_info:
            page.click(f"text={target_file_name}")

        download = download_info.value
        file_path = os.path.join(download_folder, target_file_name)
        download.save_as(file_path)
        return file_path
    else:
        return None

@pytest.mark.parametrize("download_folder", ["downloads"])
def test_file_download(download_folder):
    os.makedirs(download_folder, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        page.goto(URLS["download_page"])
        file_path = download_file(page, download_folder)

        if file_path:
            print(f"File successfully downloaded to: {file_path}")
            assert os.path.exists(file_path), f"File {file_path} does not exist"
        else:
            pytest.fail("No downloadable file found.")

        browser.close()
