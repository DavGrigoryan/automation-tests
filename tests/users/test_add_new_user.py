import allure
import pytest
import lang_massages.en.users.index as users_page_messages
from pages.users.add_page import AddPage
from tests.base_test import BaseTest


@allure.feature('Users tests')
@pytest.mark.usefixtures("clear_browser_cookies")
class TestAddNewUser(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.add_page = AddPage(browser)
        self.add_page.open()
        self.add_page.click_users_link()
        self.add_page.click_add_new_user_link()
        # Attach self.add_page to the class, so it can be accessed in test methods
        request.cls.add_page = self.add_page

    @allure.story('TC0015 - Add New User with Missing Required Fields')
    @pytest.mark.usefixtures("setup_class")
    def test_with_missing_required_fields(self):
        self.add_page.enter_user_last_name(self.get_prefix('User_1'))
        self.add_page.enter_user_email(self.get_prefix_email('user_1@example.com'))
        self.add_page.click_add_user_button()
        with allure.step('Check user added error message'):
            assert self.add_page.get_user_added_error_message == users_page_messages.get_user_added_error_message
