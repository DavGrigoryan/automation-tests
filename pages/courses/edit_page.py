import allure
from selenium.webdriver.common.by import By
from pages.courses.base_course_page import BaseCoursePage
from locators.courses.index_page_locators import IndexPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class EditPage(BaseCoursePage):
    """Page Object for the Edit Course page"""

    def __init__(self, browser):
        super().__init__(browser)

    def click_first_course_in_table(self):
        with allure.step('Click first course in table'):
            table = self.find_element(IndexPageLocators.COURSE_TABLE)
            rows = table.find_elements(By.TAG_NAME, 'tr')

            if len(rows) > 1:
                # Locate the second row (index 1 because indexing starts from 0)
                second_row = rows[1]

                # Get all the cells (td elements) within the second row
                cells = second_row.find_elements(By.TAG_NAME, 'td')

                # Ensure there are at least two cells in the second row
                if len(cells) > 1:
                    found_course = cells[0]
                    link = found_course.find_element(By.CSS_SELECTOR, 'a.es_automation_course_name')
                    link.click()

    def click_dropdown_option(self, item_text):
        with allure.step('Click dropdown option: ' + item_text):
            # Locate and click the dropdown to open it
            dropdown = self.find_element((By.CLASS_NAME, 'ui-dropdown-toggle'))
            dropdown.click()

            # Find the list item containing the provided text
            item_li = dropdown.find_element(By.XPATH, f".//li[a[contains(text(), '{item_text}')]]")

            # Click on the <a> element within the <li>
            item_li.find_element(By.TAG_NAME, 'a').click()

    def enter_delete_input(self, key):
        with allure.step('Enter delete input: ' + key):
            self.send_keys(IndexPageLocators.DELETE_VERIFY_FIELD, key, EC.visibility_of_element_located)

    def click_delete_course_button(self):
        with allure.step('Click delete course button'):
            self.click_element(IndexPageLocators.DELETE_COURSE_BTN, EC.element_to_be_clickable)

    @property
    def get_course_deleted_success_message(self):
        with allure.step('Get course deleted success message'):
            element = self.find_element(BasePageLocators.ALERT_SUCCESS_MESSAGE, EC.visibility_of_element_located)
            style_attribute = element.get_attribute("style")  # Get the value of the style attribute

            # Check if "display: none;" is not present in the style attribute and return its text if true
            if "display: none;" not in style_attribute:
                return element.text
            return None
