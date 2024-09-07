import allure
import pytest
import lang_massages.en.users.roles.index_page as roles_page_messages
from pages.users.roles.roles_page import RolesPage
from tests.base_test import BaseTest


@allure.feature('Users tests')
class TestRole(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.roles_page = RolesPage(browser)
        self.roles_page.click_sub_menu_roles()
        request.cls.roles_page = self.roles_page

    @allure.story('TC0025: Test with a successful "Add New Role" with All Valid Required Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_a_successful_add_new_role_with_all_valid_required_fields(self):
        self.roles_page.click_add_new_role_button()
        self.roles_page.enter_role_name(self.get_prefix('Role_1'))
        self.roles_page.click_save_button()
        with allure.step('Check role added success message'):
            assert self.roles_page.get_success_message == roles_page_messages.get_role_has_been_added

    @allure.story('TC0026: Test with a successful "Add New Role" with All Valid Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_a_successful_add_new_role_with_all_valid_fields(self):
        self.roles_page.refresh_page()
        self.roles_page.click_add_new_role_button()
        self.roles_page.enter_role_name(self.get_prefix('Role_2'))
        self.roles_page.enter_role_description('Test description')
        self.roles_page.click_save_button()
        with allure.step('Check role added success message'):
            assert self.roles_page.get_success_message == roles_page_messages.get_role_has_been_added

    @allure.story('TC0027: Test with Edit Role Details with All Valid Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_edit_role_details_with_all_valid_fields(self):
        self.roles_page.refresh_page()
        self.roles_page.click_first_role_edit_button()
        self.roles_page.clear_role_name_input()
        self.roles_page.enter_role_name(self.get_prefix('New Role_1'))
        self.roles_page.enter_role_description('New test description')
        self.roles_page.click_save_button()
        with allure.step('Check role updated success message'):
            assert self.roles_page.get_success_message == roles_page_messages.get_role_has_been_updated

    @allure.story('TC0028: Test Delete one Role')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_one_role(self):
        self.roles_page.refresh_page()
        self.roles_page.click_first_role_delete_button()
        self.roles_page.alert_handler('accept')
        with allure.step('Check role deleted success message'):
            assert self.roles_page.get_success_message == roles_page_messages.get_role_has_been_deleted

    # TODO: Need to remove this test and delete the second role with db connection
    @allure.story('TC0028: Test Delete one Role')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_another_role(self):
        self.roles_page.refresh_page()
        self.roles_page.click_first_role_delete_button()
        self.roles_page.alert_handler('accept')
        with allure.step('Check role deleted success message'):
            assert self.roles_page.get_success_message == roles_page_messages.get_role_has_been_deleted
