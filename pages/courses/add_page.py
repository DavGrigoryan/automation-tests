from pages.base_page import BasePage, route_app
from locators.auth.login_page_locators import LoginPageLocators
from locators.courses.add_page_locators import AddPageLocators
from selenium.webdriver.support import expected_conditions as EC
from env import config


class AddPage(BasePage):
    """Page Object for the Add Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.navigate_to(route_app('login'))
        self.enter_email(config("ADMIN_EMAIL"))
        self.enter_password(config("ADMIN_PASSWORD"))
        self.click_login_button()
        self.click_courses_link()
        self.click_add_new_course_link()
        # self.click_element(Locators.MINIMIZE_LINK_CSS)

    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def enter_course_name(self, name):
        self.send_keys(AddPageLocators.COURSE_NAME, name)

    def click_login_button(self):
        self.click_element(LoginPageLocators.SIGN_IN_BUTTON)

    def click_courses_link(self):
        self.click_element(AddPageLocators.COURSES_LINK, EC.element_to_be_clickable)

    def click_add_new_course_link(self):
        self.click_element(AddPageLocators.ADD_NEW_COURSE_LINK, EC.element_to_be_clickable)

    def click_save_button(self):
        self.scroll_to_element(AddPageLocators.SAVE_BUTTON, EC.visibility_of_element_located)
        self.click_element(AddPageLocators.SAVE_BUTTON, EC.element_to_be_clickable)

    @property
    def get_course_added_success_message(self):
        element = self.find_element(AddPageLocators.COURSE_ADDED_SUCCESS_MESSAGE, EC.visibility_of_element_located)

        # Get the value of the style attribute
        style_attribute = element.get_attribute("style")

        # Check if "display: none;" is not present in the style attribute and return its text if true
        if "display: none;" not in style_attribute:
            return element.text
        return None
