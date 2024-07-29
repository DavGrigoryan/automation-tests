import allure
from pages.courses.base_course_page import BaseCoursePage
from locators.courses.index_page_locators import IndexPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class AddPage(BaseCoursePage):
    """Page Object for the Add Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def enter_course_name(self, name):
        with allure.step('Enter course name'):
            self.send_keys(IndexPageLocators.COURSE_NAME, name)

    def click_add_new_course_link(self):
        with allure.step('Click add new course link'):
            self.click_element(IndexPageLocators.ADD_NEW_COURSE_LINK, EC.element_to_be_clickable)

    def click_save_button(self):
        with allure.step('Click save button'):
            self.scroll_to_element(IndexPageLocators.SAVE_BUTTON, EC.visibility_of_element_located)
            self.click_element(IndexPageLocators.SAVE_BUTTON, EC.element_to_be_clickable)

    @property
    def get_course_added_success_message(self):
        with allure.step('Get course added success message'):
            element = self.find_element(BasePageLocators.ALERT_SUCCESS_MESSAGE, EC.visibility_of_element_located)
            style_attribute = element.get_attribute("style")  # Get the value of the style attribute

            # Check if "display: none;" is not present in the style attribute and return its text if true
            if "display: none;" not in style_attribute:
                return element.text
            return None
