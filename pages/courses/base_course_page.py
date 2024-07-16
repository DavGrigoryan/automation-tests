from pages.base_page import BasePage
from utilities.helpers import route_app
from locators.auth.login_page_locators import LoginPageLocators
from locators.courses.add_page_locators import AddPageLocators
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import config


class BaseCoursePage(BasePage):
    """Page Object for the Add Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.navigate_to(route_app('login'))
        self.enter_email(config("ADMIN_EMAIL"))
        self.enter_password(config("ADMIN_PASSWORD"))
        self.click_login_button()

    def click_courses_link(self):
        self.click_element(AddPageLocators.COURSES_LINK, EC.element_to_be_clickable)
