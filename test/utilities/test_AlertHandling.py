from pages.AutomationDemo.alert_handler_page import AlertHandlerPage
from ..urls import URLS

def test_alert_handling(page_handler):
    alert_page = AlertHandlerPage(page_handler, URLS)

    alert_page.go_to_alert_page()
    alert_messages = alert_page.handle_cancel_alert()

    assert alert_messages, "No alert message captured"
    print("Alert message:", alert_messages[0])