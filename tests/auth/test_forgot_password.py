import allure
import pytest
import lang_massages.en.auth.login as login_page_messages
from tests.base_test import BaseTest
from utilities.config import config
from pages.auth.forgot_password_page import ForgotPasswordPage


@allure.feature('Authentications tests')
@pytest.mark.usefixtures("clear_browser_cookies")
class TestForgotPassword(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.forgot_password_page = ForgotPasswordPage(browser)
        self.forgot_password_page.open()
        # Attach self.forgot_password_page to the class, so it can be accessed in test methods
        request.cls.forgot_password_page = self.forgot_password_page

    @allure.story('TC0004 - Test with empty fields when clicking "I can\'t access my account"')
    @pytest.mark.usefixtures("setup_class")
    def test_error_massage_with_empty_fields(self):
        self.forgot_password_page.click_send_email_button()
        with allure.step('Check incomplete email error message'):
            assert self.forgot_password_page.get_error_message == login_page_messages.incomplete_email_error

    @allure.story('TC0005 - Test with a not registered email when clicking "I can\'t access my account"')
    @pytest.mark.usefixtures("setup_class")
    def test_error_message_with_not_registered_user(self):
        self.forgot_password_page.enter_email(config('NOT_REAL_EMAIL'))
        self.forgot_password_page.click_send_email_button()
        with allure.step('Check not registered email error message'):
            assert self.forgot_password_page.get_error_message == login_page_messages.not_registered_email_error
