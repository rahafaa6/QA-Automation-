from ..urls import URLS
from pages.AutomationDemo.RegistrationPage import RegistrationPage

def test_register_demo_website(page_handler):
    registration_page = RegistrationPage(page_handler)
    page_handler.goto(URLS['automation_testing_register'])
    registration_page.enter_personal_details(
        "Kareem", "Rahaf", "123 Main Street", "rahaf@gmail.com", "0598754111"
    )
    registration_page.select_gender()
    registration_page.select_hobby()
    registration_page.select_dob("2002", "January", "8")
    registration_page.select_language()
    registration_page.select_skills()
    registration_page.enter_password("123456")
    registration_page.verify_gender_selection()
    registration_page.submit_form()
    page_handler.wait_for_timeout(5000)
