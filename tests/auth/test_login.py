import pytest
import lang.login as login_page_messages
from env import config
from pages.auth.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestLogin:

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.login_page = LoginPage(browser)
        self.login_page.open()
        # Attach self.login_page to the class, so it can be accessed in test methods
        request.cls.login_page = self.login_page

    # Test case for error message when signing in with empty fields
    @pytest.mark.usefixtures("setup_class")
    def test_wrong_input_with_empty_fields(self):
        self.login_page.click_login_button()
        assert self.login_page.get_error_message == login_page_messages.login_error

    # Test case for error message when signing in with email and password that is not registered
    @pytest.mark.usefixtures("setup_class")
    def test_error_message_with_not_registered_user(self):
        self.login_page.enter_email(config('NOT_REAL_EMAIL'))
        self.login_page.enter_password(config('NOT_REAL_PASSWORD'))
        self.login_page.click_login_button()
        assert self.login_page.get_error_message == login_page_messages.login_error

    # Test case for successful sign in
    @pytest.mark.usefixtures("setup_class")
    def test_successful_sign_in(self):
        self.login_page.clear_email_input()
        self.login_page.clear_password_input()
        self.login_page.enter_email(config("ADMIN_EMAIL"))
        self.login_page.enter_password(config("ADMIN_PASSWORD"))
        self.login_page.click_login_button()
        assert self.login_page.user_is_logged_in is True
