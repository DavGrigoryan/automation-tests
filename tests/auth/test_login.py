import pytest
import lang.login as login_page_messages
from decouple import config
from pages.auth.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser)
        self.login_page.open()

    # Test case for error message when signing in with empty fields
    def test_wrong_input_with_empty_fields(self):
        self.login_page.click_login_button()
        assert self.login_page.get_error_message == login_page_messages.login_error

    # Test case for error message when signing in with email and password that is not registered
    def test_error_message_with_not_registered_user(self):
        self.login_page.enter_email(config('NOT_REAL_EMAIL'))
        self.login_page.enter_password(config('NOT_REAL_PASSWORD'))
        self.login_page.click_login_button()
        assert self.login_page.get_error_message == login_page_messages.login_error

    # Test case for successful sign in
    def test_successful_sign_in(self):
        self.login_page.enter_email(config("ADMIN_EMAIL"))
        self.login_page.enter_password(config("ADMIN_PASSWORD"))
        self.login_page.click_login_button()
        assert self.login_page.user_is_logged_in is True
