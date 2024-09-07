import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.auth.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from utilities.helpers import route_app
from utilities.config import config
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CustomBasePage(BasePage):
    def click_login_button(self):
        with allure.step('Click login button'):
            self.click_element(LoginPageLocators.SIGN_IN_BUTTON)

    def enter_email(self, email):
        with allure.step('Enter email'):
            self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        with allure.step('Enter password'):
            self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def login_as_admin(self):
        with allure.step('Navigate to login page and successfully login as admin'):
            self.navigate_to(route_app('login'))
            self.enter_email(config("ADMIN_EMAIL"))
            self.enter_password(config("ADMIN_PASSWORD"))
            self.click_login_button()

    def click_header_menu_courses_link(self):
        with allure.step('Click header courses link'):
            self.click_element(BasePageLocators.HEADER_MENU_COURSES_LINK, EC.element_to_be_clickable)

    def click_header_menu_users_link(self):
        with allure.step('Click header users link'):
            self.click_element(BasePageLocators.HEADER_MENU_USERS_LINK, EC.element_to_be_clickable)

    def click_header_menu_ojt_link(self):
        with allure.step('Click header ojt link'):
            self.click_element(BasePageLocators.HEADER_MENU_OJT_LINK, EC.element_to_be_clickable)

    def click_in_table(self, table_locator, row_locator, column_locator, link_locator,
                       row_index=1, column_index=0, action_description="Click link in table"):
        with allure.step(f'{action_description} at row {row_index + 1}, column {column_index + 1}'):
            table = self.find_element(table_locator)
            rows = self.find_child_elements(table, row_locator)

            if len(rows) > row_index:
                target_row = rows[row_index]
                cells = self.find_child_elements(target_row, column_locator)

                # Ensure there are cells in the specified row
                if len(cells) > column_index:
                    target_cell = cells[column_index]
                    link = self.find_child_element(target_cell, link_locator)
                    link.click()
                else:
                    raise Exception(f"Column {column_index + 1} does not exist in row {row_index + 1}")
            else:
                raise Exception(f"Row {row_index + 1} does not exist in the table")

    @property
    def get_success_message(self):
        with allure.step('Get success message'):
            element = self.find_element(BasePageLocators.ALERT_SUCCESS_MESSAGE, EC.visibility_of_element_located)
            style_attribute = element.get_attribute("style")  # Get the value of the style attribute

            # Check if "display: none;" is not present in the style attribute and return its text if true
            if "display: none;" not in style_attribute:
                return element.text
            return None

    def scroll_to_element_in_table(self, table_locator, element_locator, timeout=10):
        table = self.find_element(table_locator)  # Locate the table element
        element = table.find_element(*element_locator)  # Locate the target element within the table

        # Scroll horizontally within the table to bring the element into view
        self.browser.execute_script("arguments[0].scrollLeft = arguments[1].offsetLeft;", table, element)

        # Scroll vertically to the element within the table if necessary
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

        # Wait until the element is visible within the viewport
        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.execute_script(
                "return arguments[0].getBoundingClientRect().top >= 0 && "
                "arguments[0].getBoundingClientRect().bottom <= window.innerHeight;",
                element
            )
        )
