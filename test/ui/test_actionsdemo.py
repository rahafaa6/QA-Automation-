from pages.AutomationDemo.mouse_keyboard_actions_page import MouseKeyboardActionsPage
from ..urls import URLS

def test_mouse_keyboard_actions(page_handler):
    page_handler.goto(URLS["automation_testing_selectable"])
    mouse_keyboard_page = MouseKeyboardActionsPage(page_handler)

    mouse_keyboard_page.hover_and_click_switch_to()
    mouse_keyboard_page.double_click_switch_to()
    mouse_keyboard_page.right_click_switch_to()
    mouse_keyboard_page.shift_click_switch_to()
    mouse_keyboard_page.press_keys(["A", "$"])

    page_handler.wait_for_timeout(3000)