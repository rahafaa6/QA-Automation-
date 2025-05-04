from playwright.sync_api import Page
import os

class DownloadPage:
    def __init__(self, page: Page, download_folder: str):
        self.page = page
        self.download_folder = download_folder
        self.links_locator = "a"

    def find_downloadable_file(self):
        links = self.page.query_selector_all(self.links_locator)
        target_file_name = None

        for link in links:
            text = link.text_content().strip()
            if text.endswith((".txt", ".json", ".jpg", ".png")):
                target_file_name = text
                break

        return target_file_name

    def download_file(self):
        target_file_name = self.find_downloadable_file()
        if target_file_name:
            with self.page.expect_download() as download_info:
                self.page.click(f"text={target_file_name}")

            download = download_info.value
            file_path = os.path.join(self.download_folder, target_file_name)
            download.save_as(file_path)
            return file_path
        return None

    def navigate_to_page(self, url: str):
        self.page.goto(url)

    def verify_file_download(self, file_path):
        if file_path:
            print(f"File successfully downloaded to: {file_path}")
            return os.path.exists(file_path)
        return False
