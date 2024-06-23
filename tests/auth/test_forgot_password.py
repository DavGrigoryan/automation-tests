import pytest
import lang.login as login_page_messages
from env import config
from pages.auth.forgot_password_page import ForgotPasswordPage


@pytest.mark.usefixtures("browser")
class TestForgotPassword:

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.forgot_password_page = ForgotPasswordPage(browser)
        self.forgot_password_page.open()
        # Attach self.forgot_password_page to the class, so it can be accessed in test methods
        request.cls.forgot_password_page = self.forgot_password_page

    # Test case for error message when click SEND_EMAIL in with empty field
    @pytest.mark.usefixtures("setup_class")
    def test_error_massage_with_empty_fields(self):
        self.forgot_password_page.click_send_email_button()
        assert self.forgot_password_page.get_error_message == login_page_messages.incomplete_email_error

    # Test case for error message when you send an email that is not registered
    @pytest.mark.usefixtures("setup_class")
    def test_error_message_with_not_registered_user(self):
        self.forgot_password_page.enter_email(config('NOT_REAL_EMAIL'))
        self.forgot_password_page.click_send_email_button()
        assert self.forgot_password_page.get_error_message == login_page_messages.not_registered_email_error
