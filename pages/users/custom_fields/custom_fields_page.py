import allure
from pages.users.base_user_page import BaseUserPage
from locators.users.custom_fields_page_locators import CustomFieldsPageLocators as Locators
from selenium.webdriver.support import expected_conditions as EC


class CustomFieldsPage(BaseUserPage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_add_new_field_button(self):
        with allure.step('Click add new field button'):
            self.click_element(Locators.ADD_NEW_FIELD_BUTTON, EC.element_to_be_clickable)

    def enter_field_name(self, field_name):
        with allure.step('Enter field name'):
            self.send_keys(Locators.FIELD_NAME_INPUT, field_name, EC.visibility_of_element_located)

    def click_save_button(self):
        with allure.step('Click save button'):
            self.click_element(Locators.SAVE_BUTTON, EC.element_to_be_clickable)

    def click_first_field_edit_button(self):
        with allure.step('Click first field edit button'):
            self.click_element(Locators.EDIT_BUTTON, EC.element_to_be_clickable)

    def clear_field_name_input(self):
        with allure.step('Clear field name'):
            self.clear_input(Locators.FIELD_NAME_INPUT, EC.visibility_of_element_located)

    def click_first_field_delete_button(self):
        with allure.step('Click first field delete button'):
            self.click_element(Locators.DELETE_BUTTON, EC.element_to_be_clickable)
