import allure
from pages.users.base_user_page import BaseUserPage
from locators.users.index_page_locators import IndexPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class EditPage(BaseUserPage):
    def __init__(self, browser):
        super().__init__(browser)

    def enter_filter_search_by_name_or_email(self, email):
        with allure.step('Enter filter search by name or email: ' + email):
            self.send_keys(BasePageLocators.FILTER_SEARCH_BY_NAME_OR_EMAIL, email, EC.visibility_of_element_located)

    def click_apply_filters_button(self):
        with allure.step('Click apply filters button'):
            self.click_element(BasePageLocators.FILTER_APPLY_FILTERS_BUTTON, EC.element_to_be_clickable)

    def click_check_all_checkbox(self):
        with allure.step('Click users checkbox check all'):
            self.click_element(IndexPageLocators.CHECK_ALL_CHECKBOX, EC.element_to_be_clickable)

    def click_delete_selected_users(self):
        with allure.step('Click delete selected users button'):
            self.click_element(IndexPageLocators.DELETE_SELECTED_USERS, EC.element_to_be_clickable)

    def click_first_user_in_table(self):
        table_locator = IndexPageLocators.USERS_TABLE
        row_locator = BasePageLocators.TAG_TR
        column_locator = BasePageLocators.TAG_TD
        link_locator = IndexPageLocators.USER_NAME_LINK
        with allure.step('Click first user in table'):
            self.click_in_table(table_locator, row_locator, column_locator, link_locator, 1, 2)

    def click_first_link_in_wizard_steps(self):
        with allure.step('Click first link in wizard steps'):
            wizard_steps = self.find_element(IndexPageLocators.WIZARD_STEPS)
            first_link = self.find_child_element(wizard_steps, BasePageLocators.TAG_A)
            first_link.click()

    def click_edit_user_link(self):
        with allure.step('Click Edit User link'):
            parent_div = self.find_element(IndexPageLocators.TABLE_INFO_OF_USER)
            edit_user_link = self.find_child_element(parent_div, BasePageLocators.TAG_A)
            edit_user_link.click()

    def click_save_changes_button(self):
        with allure.step('Click save changes button'):
            self.scroll_to_element(IndexPageLocators.SAVE_CHANGES_BUTTON, EC.visibility_of_element_located)
            self.click_element(IndexPageLocators.SAVE_CHANGES_BUTTON, EC.element_to_be_clickable)

    @property
    def get_profile_saved_success_message(self):
        with allure.step('Get the profile saved success message '):
            element = self.find_element(BasePageLocators.ALERT_SUCCESS_MESSAGE, EC.visibility_of_element_located)
            return element.text
