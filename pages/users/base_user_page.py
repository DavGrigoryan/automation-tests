import allure
from pages.custom_base_page import CustomBasePage
from utilities.db_utils import fetch_one
from locators.users.index_page_locators import IndexPageLocators
from selenium.webdriver.support import expected_conditions as EC


class BaseUserPage(CustomBasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.login_as_admin()

    def enter_user_first_name(self, name):
        with allure.step('Enter user first name'):
            self.send_keys(IndexPageLocators.USER_FIRST_NAME, name, EC.visibility_of_element_located)

    def enter_user_last_name(self, name):
        with allure.step('Enter user last name'):
            self.send_keys(IndexPageLocators.USER_LAST_NAME, name, EC.visibility_of_element_located)

    def enter_user_email(self, email):
        with allure.step('Enter user email'):
            self.send_keys(IndexPageLocators.USER_EMAIL, email, EC.visibility_of_element_located)

    def clear_user_first_name_input(self):
        with allure.step('Clear first name input'):
            self.scroll_to_element(IndexPageLocators.USER_FIRST_NAME, EC.visibility_of_element_located)
            self.clear_input(IndexPageLocators.USER_FIRST_NAME)

    def clear_user_last_name_input(self):
        with allure.step('Clear last name input'):
            self.scroll_to_element(IndexPageLocators.USER_LAST_NAME, EC.visibility_of_element_located)
            self.clear_input(IndexPageLocators.USER_LAST_NAME)

    def clear_user_email_input(self):
        with allure.step('Clear email input'):
            self.scroll_to_element(IndexPageLocators.USER_EMAIL, EC.visibility_of_element_located)
            self.clear_input(IndexPageLocators.USER_EMAIL)

    @staticmethod
    def check_user_exists(email):
        with allure.step('Check if user exists in database'):
            query = "SELECT COUNT(*) FROM users WHERE email = %s"
            params = (email,)
            result = fetch_one(query, params)
            return result['COUNT(*)'] > 0 if result else False

    def click_sub_menu_roles(self):
        with allure.step('Click sub menu roles link'):
            self.click_element(IndexPageLocators.SUB_MENU_ROLES_LINK, EC.element_to_be_clickable)

    def click_sub_menu_user_groups(self):
        with allure.step('Click sub menu user groups link'):
            self.click_element(IndexPageLocators.SUB_MENU_USER_GROUPS_LINK, EC.element_to_be_clickable)

    def click_sub_menu_custom_fields(self):
        with allure.step('Click sub menu custom fields link'):
            self.click_element(IndexPageLocators.SUB_MENU_CUSTOM_FIELDS_LINK, EC.element_to_be_clickable)
