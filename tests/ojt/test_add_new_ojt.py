import time

import allure
import pytest
import lang_massages.en.users.custom_fields.index_page as custom_fields_messages
from pages.ojt.add_page import AddPage
from tests.base_test import BaseTest


@allure.feature('OJT tests')
@pytest.mark.usefixtures("clear_browser_cookies")
class TestAddNewOjt(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.add_page = AddPage(browser)
        self.add_page.open()
        self.add_page.click_header_menu_ojt_link()
        request.cls.add_page = self.add_page

    @allure.story('TC0036: Add OJT with All Required Fields Filled')
    @pytest.mark.usefixtures("setup_class")
    def test_add_ojt_with_all_required_fields_filled(self):
        self.add_page.click_manual_add_button()
        time.sleep(5)
        # self.add_page.enter_field_name(self.get_prefix('Field_1'))
        # self.add_page.click_save_button()
        # with allure.step('Check field added success message'):
        #     assert self.add_page.get_success_message == custom_fields_messages.get_field_has_been_added

    # @allure.story('TC0034: Test with Edit Custom Fields Details with All Valid Fields')
    # @pytest.mark.usefixtures("setup_class")
    # def test_with_edit_custom_fields_details_with_all_valid_fields(self):
    #     self.add_page.click_first_field_edit_button()
    #     self.add_page.clear_field_name_input()
    #     self.add_page.enter_field_name(self.get_prefix('New field_1'))
    #     self.add_page.click_save_button()
    #     with allure.step('Check field updated success message'):
    #         assert self.add_page.get_success_message == custom_fields_messages.get_field_has_been_updated
    #
    # @allure.story('TC0035: Test Delete the Custom Field')
    # @pytest.mark.usefixtures("setup_class")
    # def test_delete_the_custom_field(self):
    #     self.add_page.click_first_field_delete_button()
    #     self.add_page.alert_handler('accept')
    #     with allure.step('Check field deleted success message'):
    #         assert self.add_page.get_success_message == custom_fields_messages.get_field_has_been_deleted
