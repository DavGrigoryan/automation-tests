from pages.base_page import BasePage
from utilities.helpers import route_app
from locators.auth.forgot_password_page_locators import ForgotPasswordPageLocators as Locators
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage(BasePage):
    """Page Object for the Forgot Password page"""

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.navigate_to(route_app('login'))
        self.scroll_to_element(Locators.I_CANNOT_ACCESS_MY_ACCOUNT_LINK, EC.visibility_of_element_located)
        self.click_element(Locators.I_CANNOT_ACCESS_MY_ACCOUNT_LINK, EC.element_to_be_clickable)

    def enter_email(self, email):
        self.send_keys(Locators.EMAIL_INPUT, email)

    def click_send_email_button(self):
        self.scroll_to_element(Locators.SEND_EMAIL_BUTTON, EC.visibility_of_element_located)
        self.click_element(Locators.SEND_EMAIL_BUTTON)

    @property
    def get_error_message(self):
        self.scroll_to_element(Locators.ERROR_MESSAGE, EC.visibility_of_element_located)
        element = self.find_element(Locators.ERROR_MESSAGE, EC.visibility_of_element_located)
        class_name = element.get_attribute("class")  # Get the class attribute of the element

        # Check if the element has the desired class and return its text if true
        if class_name == 'alert alert-danger':
            return element.text
        return None
