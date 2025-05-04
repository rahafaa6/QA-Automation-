import pytest
import os
from pages.OrangeHRM.LoginPage import LoginPageWithMedia
from ..urls import URLS

@pytest.fixture(scope="session")
def setup_directories():
    os.makedirs('screenshots', exist_ok=True)
    os.makedirs('reports/videos', exist_ok=True)

def test_login_screenshots_and_video(page_handler, setup_directories):
    login_page = LoginPageWithMedia(page_handler, URLS)

    login_page.go_to_login_page()
    login_page.perform_login('Admin', 'admin123')

    if login_page.check_video_saved():
        print("Video saved to: reports/videos/login_video.mp4")
    else:
        print("No video recorded.")
