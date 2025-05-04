class AlertHandlerPage:
    def __init__(self, page_handler, urls):
        self.page_handler = page_handler
        self.urls = urls
        self.locators = {
            "cancel_tab_link": '//a[@href="#CancelTab"]',
            "cancel_button": '//div[@id="CancelTab"]/button'
        }

    def go_to_alert_page(self):
        self.page_handler.goto(self.urls["automation_testing_alerts"])

    def handle_cancel_alert(self):
        alert_messages = []

        def on_dialog(dialog):
            message = dialog.message
            alert_messages.append(message)
            dialog.accept()

        self.page_handler.on("dialog", on_dialog)
        self.page_handler.wait_for_selector(self.locators["cancel_tab_link"]).click()
        self.page_handler.wait_for_timeout(2000)
        self.page_handler.wait_for_selector(self.locators["cancel_button"]).click()
        self.page_handler.wait_for_timeout(3000)

        return alert_messages
