import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class BaseUserPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Navigate to login page and successfully login as admin'):
            self.login_as_admin()

    def click_users_link(self):
        with allure.step('Click header users link'):
            self.click_element(BasePageLocators.HEADER_MENU_USERS_LINK, EC.element_to_be_clickable)
