import time

import allure
from pages.users.base_user_page import BaseUserPage
from locators.users.user_groups_page_locators import UserGroupsPageLocators as Locators
from selenium.webdriver.support import expected_conditions as EC


class UserGroupsPage(BaseUserPage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_add_new_user_group_button(self):
        with allure.step('Click add new user group button'):
            self.click_element(Locators.ADD_NEW_USER_GROUP_LINK, EC.element_to_be_clickable)

    def enter_user_group_name(self, name):
        with allure.step('Enter user group name'):
            self.send_keys(Locators.USER_GROUP_NAME_INPUT, name, EC.visibility_of_element_located)

    def enter_user_group_description(self, description):
        with allure.step('Enter user group description'):
            self.send_keys(Locators.USER_GROUP_DESCRIPTION_INPUT, description, EC.visibility_of_element_located)

    def click_add_user_group_button(self):
        with allure.step('Click add user group button'):
            self.click_element(Locators.ADD_USER_GROUP_BUTTON, EC.element_to_be_clickable)

    def scroll_first_user_group_edit_button(self):
        with allure.step('Scroll first user group edit button'):
            self.scroll_by_amount(100, 100)

    def click_first_user_group_edit_button(self):
        with allure.step('Click first user group edit button'):
            self.wait_for_element(Locators.EDIT_BUTTON, EC.element_to_be_clickable)
            self.scroll_to_bottom()
            self.click_element(Locators.EDIT_BUTTON, EC.element_to_be_clickable)

    def clear_edit_name_input(self):
        with allure.step('Clear user group name'):
            self.clear_input(Locators.EDIT_NAME_INPUT, EC.visibility_of_element_located)

    def clear_edit_description_input(self):
        with allure.step('Clear user group description'):
            self.clear_input(Locators.EDIT_DESCRIPTION_INPUT, EC.visibility_of_element_located)

    def enter_edit_name(self, name):
        with allure.step('Enter user group edit name'):
            self.send_keys(Locators.EDIT_NAME_INPUT, name, EC.visibility_of_element_located)

    def enter_edit_description(self, description):
        with allure.step('Enter user group edit description'):
            self.send_keys(Locators.EDIT_DESCRIPTION_INPUT, description, EC.visibility_of_element_located)

    def click_first_user_group_delete_button(self):
        with allure.step('Click first user group delete button'):
            self.wait_for_element(Locators.DELETE_BUTTON, EC.element_to_be_clickable)
            self.scroll_to_bottom()
            self.scroll_to_element_in_table(Locators.TABLE_USER_GROUPS, Locators.DELETE_BUTTON)
            self.click_element(Locators.DELETE_BUTTON, EC.element_to_be_clickable)
