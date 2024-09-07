import allure
import pytest
import lang_massages.en.users.index as users_messages
from pages.users.users.edit_page import EditPage
from tests.base_test import BaseTest
import lang_massages.en.users.index as users_page_messages


@allure.feature('Users tests')
class TestEditUser(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.edit_page = EditPage(browser)
        request.cls.edit_page = self.edit_page

    @allure.story('TC0021: Test with Edit User Details with All Valid Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_edit_user_details(self):
        self.edit_page.enter_filter_search_by_name_or_email(self.get_prefix_email('user_1@example.com'))
        self.edit_page.click_apply_filters_button()
        self.edit_page.click_first_user_in_table()
        self.edit_page.click_first_link_in_wizard_steps()
        self.edit_page.click_edit_user_link()
        self.edit_page.clear_user_first_name_input()
        self.edit_page.enter_user_first_name(self.get_prefix_email('Test_1'))
        self.edit_page.clear_user_last_name_input()
        self.edit_page.enter_user_last_name(self.get_prefix_email('Testing'))
        self.edit_page.clear_user_email_input()
        self.edit_page.enter_user_email(self.get_prefix_email('john.smith@example.com'))
        self.edit_page.click_save_changes_button()

        with allure.step('Check the profile saved success message'):
            assert (
                    self.edit_page.get_profile_saved_success_message
                    == users_page_messages.get_user_saved_success_message
            )

    @allure.story('TC0020: Test Delete one user')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_one_user(self):
        self.edit_page.click_header_menu_users_link()
        self.edit_page.enter_filter_search_by_name_or_email(self.get_prefix_email('user_2@example.com'))
        self.edit_page.click_apply_filters_button()
        self.edit_page.click_check_all_checkbox()
        self.edit_page.click_delete_selected_users()
        self.edit_page.alert_handler('accept')

        with allure.step('Check if user has been deleted successfully'):
            assert self.edit_page.get_success_message == users_messages.get_user_deleted_success_message

    @allure.story('TC0019: Test Delete all users')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_all_users(self):
        self.edit_page.click_header_menu_users_link()
        self.edit_page.click_check_all_checkbox()
        self.edit_page.click_delete_selected_users()
        self.edit_page.alert_handler('accept')

        with allure.step('Check if users has been deleted successfully'):
            assert self.edit_page.get_success_message == users_messages.get_user_deleted_success_message
