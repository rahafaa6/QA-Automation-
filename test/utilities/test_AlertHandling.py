import pytest
from playwright.sync_api import sync_playwright
from ..urls import URLS

@pytest.fixture(scope="function")
def setup_and_teardown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_alert_handling(setup_and_teardown):
    page = setup_and_teardown
    text_alert = []

    def handle_dialog(dialog):
        message = dialog.message
        text_alert.append(message)
        dialog.accept()

    page.goto(URLS["automation_testing_alerts"])

    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(2000)

    page.on("dialog", handle_dialog)

    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(3000)
    assert text_alert, "No alert message captured"
    print("Alert message:", text_alert[0])
