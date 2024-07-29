import allure
from pages.base_page import BasePage
from utilities.helpers import route_app
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from utilities.config import config


class BaseCoursePage(BasePage):
    """Page Object for the Add Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Login and open courses page'):
            self.navigate_to(route_app('login'))
            self.enter_email(config("ADMIN_EMAIL"))
            self.enter_password(config("ADMIN_PASSWORD"))
            self.click_login_button()

    def click_courses_link(self):
        with allure.step('Click header courses link'):
            self.click_element(BasePageLocators.HEADER_MENU_COURSES_LINK, EC.element_to_be_clickable)
