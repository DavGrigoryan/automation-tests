from pages.courses.base_course_page import BaseCoursePage
from locators.courses.add_page_locators import AddPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class AddPage(BaseCoursePage):
    """Page Object for the Add Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def enter_course_name(self, name):
        self.send_keys(AddPageLocators.COURSE_NAME, name)

    def click_add_new_course_link(self):
        self.click_element(AddPageLocators.ADD_NEW_COURSE_LINK, EC.element_to_be_clickable)

    def click_save_button(self):
        self.scroll_to_element(AddPageLocators.SAVE_BUTTON, EC.visibility_of_element_located)
        self.click_element(AddPageLocators.SAVE_BUTTON, EC.element_to_be_clickable)

    @property
    def get_course_added_success_message(self):
        element = self.find_element(BasePageLocators.ALERT_SUCCESS_MESSAGE, EC.visibility_of_element_located)
        style_attribute = element.get_attribute("style")  # Get the value of the style attribute

        # Check if "display: none;" is not present in the style attribute and return its text if true
        if "display: none;" not in style_attribute:
            return element.text
        return None
