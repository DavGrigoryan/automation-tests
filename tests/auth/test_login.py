import pytest
import lang_massages.en.auth.login as login_page_messages
from tests.base_test import BaseTest
from utilities.config import config
from pages.auth.login_page import LoginPage


@pytest.mark.usefixtures("clear_browser_cookies")
class TestLogin(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.login_page = LoginPage(browser)
        self.login_page.open()
        # Attach self.login_page to the class, so it can be accessed in test methods
        request.cls.login_page = self.login_page

    # TC0001 - Test login with empty fields
    @pytest.mark.usefixtures("setup_class")
    def test_login_with_empty_fields(self):
        self.login_page.click_login_button()
        assert self.login_page.get_error_message == login_page_messages.login_error

    # TC0002 - Test login with invalid email and password
    @pytest.mark.usefixtures("setup_class")
    def test_login_with_invalid_email_and_password(self):
        self.login_page.enter_email(config('NOT_REAL_EMAIL'))
        self.login_page.enter_password(config('NOT_REAL_PASSWORD'))
        self.login_page.click_login_button()
        assert self.login_page.get_error_message == login_page_messages.login_error

    # TC0003 - Test with a successful login
    @pytest.mark.usefixtures("setup_class")
    def test_with_a_successful_login(self):
        self.login_page.clear_email_input()
        self.login_page.clear_password_input()
        self.login_page.enter_email(config("ADMIN_EMAIL"))
        self.login_page.enter_password(config("ADMIN_PASSWORD"))
        self.login_page.click_login_button()
        assert self.login_page.user_is_logged_in is True
