import allure
import pytest
import lang_massages.en.users.index as users_page_messages
from pages.users.users.add_page import AddPage
from tests.base_test import BaseTest


@allure.feature('Users tests')
class TestAddNewUser(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.add_page = AddPage(browser)
        self.add_page.click_header_menu_users_link()
        request.cls.add_page = self.add_page

    @allure.story('TC0022: Test with empty fields Add New User with Missing Required Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_missing_required_fields(self):
        self.add_page.click_add_new_user_link()
        self.add_page.enter_user_last_name(self.get_prefix('User_1'))
        self.add_page.enter_user_email(self.get_prefix_email('user_1@example.com'))
        self.add_page.click_add_user_button()
        with allure.step('Check user added error message'):
            assert self.add_page.get_user_added_error_message == users_page_messages.get_user_added_error_message

    @allure.story('TC0023: Test with a successful Add New User with Optional Fields Filled In')
    @pytest.mark.usefixtures("setup_class")
    def test_with_successful_add_new_user_with_optional_fields(self):
        self.add_page.click_header_menu_users_link()
        self.add_page.click_add_new_user_link()
        self.add_page.select_user_title('Mr.')
        self.add_page.enter_user_first_name(self.get_prefix('John'))
        self.add_page.clear_user_last_name_input()
        self.add_page.enter_user_last_name(self.get_prefix('Doe'))
        self.add_page.clear_user_email_input()
        user_email = self.get_prefix_email('user_1@example.com')
        self.add_page.enter_user_email(user_email)
        self.add_page.click_add_user_button()

        with allure.step('Check user added success message'):
            assert self.add_page.get_user_added_success_message == users_page_messages.get_user_added_success_message

        assert self.add_page.check_user_exists(user_email) is True

    @allure.story('TC0024: Test with a successful Add New User with All Valid Required Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_successful_add_new_user_with_all_valid_fields(self):
        self.add_page.click_header_menu_users_link()
        self.add_page.click_add_new_user_link()
        self.add_page.enter_user_first_name(self.get_prefix('John'))
        self.add_page.enter_user_last_name(self.get_prefix('Doe'))
        self.add_page.clear_user_email_input()
        user_email = self.get_prefix_email('user_2@example.com')
        self.add_page.enter_user_email(user_email)
        self.add_page.click_add_user_button()

        with allure.step('Check user added success message'):
            assert self.add_page.get_user_added_success_message == users_page_messages.get_user_added_success_message

        assert self.add_page.check_user_exists(user_email) is True
