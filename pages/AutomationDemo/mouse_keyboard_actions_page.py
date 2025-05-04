class MouseKeyboardActionsPage:
    def __init__(self, page_handler):
        self.page_handler = page_handler
        self.locators = {
            "switch_to_link": '//a[text()="SwitchTo"]'
        }

    def hover_and_click_switch_to(self):
        switch_to = self.page_handler.locator(self.locators["switch_to_link"])
        switch_to.hover()
        switch_to.click()

    def double_click_switch_to(self):
        switch_to = self.page_handler.locator(self.locators["switch_to_link"])
        switch_to.dblclick()

    def right_click_switch_to(self):
        switch_to = self.page_handler.locator(self.locators["switch_to_link"])
        switch_to.click(button="right")

    def shift_click_switch_to(self):
        switch_to = self.page_handler.locator(self.locators["switch_to_link"])
        switch_to.click(modifiers=["Shift"])

    def press_keys(self, keys):
        for key in keys:
            self.page_handler.keyboard.press(key)