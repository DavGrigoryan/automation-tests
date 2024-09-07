import allure
from pages.users.base_user_page import BaseUserPage
from locators.users.roles_page_locators import RolesPageLocators
from selenium.webdriver.support import expected_conditions as EC


class RolesPage(BaseUserPage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_add_new_role_button(self):
        with allure.step('Click add new role button'):
            self.click_element(RolesPageLocators.ADD_NEW_ROLE_BUTTON, EC.element_to_be_clickable)

    def enter_role_name(self, role_name):
        with allure.step('Enter role name'):
            self.send_keys(RolesPageLocators.ADD_NAME_INPUT, role_name, EC.visibility_of_element_located)

    def enter_role_description(self, role_description):
        with allure.step('Enter role description'):
            self.send_keys(RolesPageLocators.ADD_DESCRIPTION_INPUT, role_description, EC.visibility_of_element_located)

    def click_save_button(self):
        with allure.step('Click save button'):
            self.click_element(RolesPageLocators.SAVE_BUTTON, EC.element_to_be_clickable)

    def click_first_role_edit_button(self):
        with allure.step('Click first role edit button'):
            self.click_element(RolesPageLocators.EDIT_BUTTON, EC.element_to_be_clickable)

    def click_first_role_delete_button(self):
        with allure.step('Click first role delete button'):
            self.click_element(RolesPageLocators.DELETE_BUTTON, EC.element_to_be_clickable)

    def clear_role_name_input(self):
        with allure.step('Clear role name'):
            self.clear_input(RolesPageLocators.ADD_NAME_INPUT, EC.visibility_of_element_located)
