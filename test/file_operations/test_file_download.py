import pytest
import os
from ..urls import URLS
from pages.Other.download_page import DownloadPage

@pytest.mark.parametrize("download_folder", ["downloads"])
def test_file_download(page_handler, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    download_page = DownloadPage(page_handler, download_folder)
    download_page.navigate_to_page(URLS["download_page"])
    file_path = download_page.download_file()
    assert download_page.verify_file_download(file_path), "File was not downloaded successfully."
