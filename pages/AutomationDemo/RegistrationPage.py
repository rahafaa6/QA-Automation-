class RegistrationPage:
    def __init__(self, page_handler):
        self.page_handler = page_handler
        self.register_locators = {
            "first_name": '//input[@placeholder="First Name"]',
            "last_name": '//input[@placeholder="Last Name"]',
            "address": '//textarea[@ng-model="Adress"]',
            "email": '//input[@ng-model="EmailAdress"]',
            "phone": '//input[@ng-model="Phone"]',
            "gender_male": '//input[@value="Male"]',
            "hobby_cricket": '//input[@value="Cricket"]',
            "country": '//select[@id="country"]',
            "year": '//select[@id="yearbox"]',
            "month": '//select[@ng-model="monthbox"]',
            "day": '//select[@id="daybox"]',
            "languages_dropdown": '//div[@id="msdd"]',
            "language_arabic": '//a[text()="Arabic"]',
            "skills": '//select[@id="Skills"]',
            "password": '//input[@id="firstpassword"]',
            "confirm_password": '//input[@id="secondpassword"]',
            "submit": 'button[type="submit"]',
        }

    def enter_personal_details(self, first_name, last_name, address, email, phone):
        self.page_handler.type(self.register_locators['first_name'], first_name)
        self.page_handler.type(self.register_locators['last_name'], last_name)
        self.page_handler.type(self.register_locators['address'], address)
        self.page_handler.type(self.register_locators['email'], email)
        self.page_handler.type(self.register_locators['phone'], phone)

    def select_gender(self, gender="Male"):
        gender_selector = self.page_handler.locator(self.register_locators['gender_male'])
        gender_selector.click()

    def select_hobby(self, hobby="Cricket"):
        hobby_selector = self.page_handler.locator(self.register_locators['hobby_cricket'])
        hobby_selector.click()

    def select_dob(self, year, month, day):
        self.page_handler.select_option(self.register_locators['year'], year)
        self.page_handler.select_option(self.register_locators['month'], month)
        self.page_handler.select_option(self.register_locators['day'], day)

    def select_language(self, language="Arabic"):
        self.page_handler.locator(self.register_locators['languages_dropdown']).click()
        self.page_handler.locator(self.register_locators['language_arabic']).click()

    def select_skills(self, skills="iOS"):
        self.page_handler.select_option(self.register_locators['skills'], label=skills)

    def enter_password(self, password):
        self.page_handler.type(self.register_locators['password'], password)
        self.page_handler.type(self.register_locators['confirm_password'], password)

    def submit_form(self):
        self.page_handler.click(self.register_locators['submit'])

    def verify_gender_selection(self):
        gender = self.page_handler.locator(self.register_locators['gender_male'])
        assert gender.is_checked(), "Gender was not selected"

