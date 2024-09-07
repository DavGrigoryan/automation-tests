import time

import allure
import pytest
import lang_massages.en.users.user_groups.index_page as user_group_messages
from pages.users.user_groups.user_groups_page import UserGroupsPage
from tests.base_test import BaseTest


@allure.feature('Users tests')
class TestUserGroups(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.user_groups_page = UserGroupsPage(browser)
        self.user_groups_page.click_sub_menu_user_groups()
        request.cls.user_groups_page = self.user_groups_page

    @allure.story('TC0029: Test with a successful "Add User Groups" with All Valid Required Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_successful_add_new_user_group_with_all_valid_fields(self):
        self.user_groups_page.click_add_new_user_group_button()
        self.user_groups_page.enter_user_group_name(self.get_prefix('User_group_1'))
        self.user_groups_page.click_add_user_group_button()
        with allure.step('Check user group added success message'):
            assert self.user_groups_page.get_success_message == user_group_messages.get_user_group_has_been_added

    @allure.story('TC0030: Test with a successful "Add User Group" with All Valid Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_a_successful_add_new_user_group_with_all_valid_fields(self):
        self.user_groups_page.refresh_page()
        self.user_groups_page.click_add_new_user_group_button()
        self.user_groups_page.enter_user_group_name(self.get_prefix('User_group_2'))
        self.user_groups_page.enter_user_group_description('Test description 2')
        self.user_groups_page.click_add_user_group_button()
        with allure.step('Check user group added success message'):
            assert self.user_groups_page.get_success_message == user_group_messages.get_user_group_has_been_added

    @allure.story('TC0031: Test with Edit User Group with All Valid Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_edit_user_group_with_all_valid_fields(self):
        self.user_groups_page.refresh_page()
        self.user_groups_page.click_first_user_group_edit_button()
        self.user_groups_page.clear_edit_name_input()
        self.user_groups_page.enter_edit_name(self.get_prefix('New user_group_2'))
        self.user_groups_page.clear_edit_description_input()
        self.user_groups_page.enter_edit_description('New test description')
        self.user_groups_page.click_add_user_group_button()
        with allure.step('Check user group updated success message'):
            assert self.user_groups_page.get_success_message == user_group_messages.get_user_group_has_been_updated

    @allure.story('TC0032: Test Delete one User Group')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_one_user_group(self):
        self.user_groups_page.refresh_page()
        self.user_groups_page.click_first_user_group_delete_button()
        self.user_groups_page.alert_handler('accept')
        with allure.step('Check user group deleted success message'):
            assert self.user_groups_page.get_success_message == user_group_messages.get_user_group_has_been_deleted

    # TODO: Need to remove this test and delete the second user_group with db connection
    @allure.story('TC0032: Test Delete one User Group')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_another_user_group(self):
        self.user_groups_page.refresh_page()
        self.user_groups_page.click_first_user_group_delete_button()
        self.user_groups_page.alert_handler('accept')
        with allure.step('Check user group deleted success message'):
            assert self.user_groups_page.get_success_message == user_group_messages.get_user_group_has_been_deleted
