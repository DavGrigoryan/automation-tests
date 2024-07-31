import allure
from pages.users.base_user_page import BaseUserPage
from locators.users.index_page_locators import IndexPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class AddPage(BaseUserPage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_add_new_user_link(self):
        with allure.step('Click add new course link'):
            self.click_element(IndexPageLocators.ADD_NEW_USER_LINK, EC.element_to_be_clickable)

    def enter_user_last_name(self, name):
        with allure.step('Enter user last name'):
            self.send_keys(IndexPageLocators.USER_LAST_NAME, name, EC.visibility_of_element_located)

    def enter_user_email(self, email):
        with allure.step('Enter user email'):
            self.send_keys(IndexPageLocators.USER_EMAIL, email, EC.visibility_of_element_located)

    def click_add_user_button(self):
        with allure.step('Click add user button'):
            self.scroll_to_element(IndexPageLocators.ADD_USER_BUTTON, EC.visibility_of_element_located)
            self.click_element(IndexPageLocators.ADD_USER_BUTTON, EC.element_to_be_clickable)

    @property
    def get_user_added_error_message(self):
        with allure.step('Get user added error message'):
            element = self.find_element(BasePageLocators.ALERT_DANGER_MESSAGE, EC.visibility_of_element_located)
            return element.text
