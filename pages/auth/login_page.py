from pages.base_page import BasePage
from utilities.helpers import route_app
from locators.auth.login_page_locators import LoginPageLocators as Locators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    """Page Object for the Login page"""

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.navigate_to(route_app('login'))

    def clear_email_input(self):
        self.clear_input(Locators.EMAIL_INPUT)

    def clear_password_input(self):
        self.clear_input(Locators.PASSWORD_INPUT)

    @property
    def get_error_message(self):
        element = self.find_element(Locators.ERROR_MESSAGE, EC.visibility_of_element_located)
        class_name = element.get_attribute("class")

        # Check if the element has the desired class and return its text if true
        if class_name == 'alert alert-danger':
            return element.text
        return None

    @property
    def user_is_logged_in(self):
        return self.is_element_found(Locators.IS_LOGGED_IN, EC.presence_of_element_located)
