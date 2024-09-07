import allure
import pytest
import lang_massages.en.users.custom_fields.index_page as custom_fields_messages
from pages.users.custom_fields.custom_fields_page import CustomFieldsPage
from tests.base_test import BaseTest


@allure.feature('Users tests')
@pytest.mark.usefixtures("clear_browser_cookies")
class TestCustomFields(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.custom_fields_page = CustomFieldsPage(browser)
        self.custom_fields_page.open()
        self.custom_fields_page.click_header_menu_users_link()
        self.custom_fields_page.click_sub_menu_custom_fields()
        request.cls.custom_fields_page = self.custom_fields_page

    @allure.story('TC0033: Test with a successful "Add New Custom Fields" with All Valid Required Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_a_successful_add_new_custom_fields_with_all_valid_required_fields(self):
        self.custom_fields_page.click_add_new_field_button()
        self.custom_fields_page.enter_field_name(self.get_prefix('Field_1'))
        self.custom_fields_page.click_save_button()
        with allure.step('Check field added success message'):
            assert self.custom_fields_page.get_success_message == custom_fields_messages.get_field_has_been_added

    @allure.story('TC0034: Test with Edit Custom Fields Details with All Valid Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_edit_custom_fields_details_with_all_valid_fields(self):
        self.custom_fields_page.click_first_field_edit_button()
        self.custom_fields_page.clear_field_name_input()
        self.custom_fields_page.enter_field_name(self.get_prefix('New field_1'))
        self.custom_fields_page.click_save_button()
        with allure.step('Check field updated success message'):
            assert self.custom_fields_page.get_success_message == custom_fields_messages.get_field_has_been_updated

    @allure.story('TC0035: Test Delete the Custom Field')
    @pytest.mark.usefixtures("setup_class")
    def test_delete_the_custom_field(self):
        self.custom_fields_page.click_first_field_delete_button()
        self.custom_fields_page.alert_handler('accept')
        with allure.step('Check field deleted success message'):
            assert self.custom_fields_page.get_success_message == custom_fields_messages.get_field_has_been_deleted
