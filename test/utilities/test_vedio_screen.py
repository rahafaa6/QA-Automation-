import os
import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="session")
def setup_directories():
    os.makedirs('screenshots', exist_ok=True)
    os.makedirs('reports/videos', exist_ok=True)

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir='reports/videos')
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_login_screenshots_and_video(setup_directories, browser_context):
    page = browser_context
    page.goto(URLS["orangehrm"])
    page.wait_for_selector('//input[@name="username"]').fill('Admin')
    page.wait_for_selector('//input[@name="password"]').fill('admin123')
    page.screenshot(path='screenshots/login_page.png')
    page.query_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)
    page.screenshot(path='screenshots/homepage.png')
    video_path = 'reports/videos/login_video.mp4'
    if os.path.exists(video_path):
        print(f"Video saved to: {video_path}")
    else:
        print("No video recorded.")
