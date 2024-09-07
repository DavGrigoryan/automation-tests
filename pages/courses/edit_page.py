import allure
from pages.courses.base_course_page import BaseCoursePage
from locators.courses.index_page_locators import IndexPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class EditPage(BaseCoursePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_first_course_in_table(self):
        table_locator = IndexPageLocators.COURSE_TABLE
        row_locator = BasePageLocators.TAG_TR
        column_locator = BasePageLocators.TAG_TD
        link_locator = IndexPageLocators.COURSE_NAME_LINK
        with allure.step('Click first course in table'):
            self.click_in_table(table_locator, row_locator, column_locator, link_locator, 1, 0)

    def click_dropdown_option(self, item_text):
        with allure.step('Click dropdown option: ' + item_text):
            # Locate and click the dropdown to open it
            dropdown = self.find_element(IndexPageLocators.DROPDOWN_TOGGLE)
            dropdown.click()

            # Find the list item containing the provided text
            item_li = dropdown.find_element(*IndexPageLocators.dropdown_option(item_text))

            # Click on the <a> element within the <li>
            item_li.find_element(*IndexPageLocators.DROPDOWN_ITEMS).click()

    def enter_delete_input(self, key):
        with allure.step('Enter delete input: ' + key):
            self.send_keys(IndexPageLocators.DELETE_VERIFY_FIELD, key, EC.visibility_of_element_located)

    def click_delete_course_button(self):
        with allure.step('Click delete course button'):
            self.click_element(IndexPageLocators.DELETE_COURSE_BTN, EC.element_to_be_clickable)
