import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class BaseCoursePage(BasePage):
    """Page Object for the Add Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.login_as_admin()

    def click_courses_link(self):
        with allure.step('Click header courses link'):
            self.click_element(BasePageLocators.HEADER_MENU_COURSES_LINK, EC.element_to_be_clickable)
