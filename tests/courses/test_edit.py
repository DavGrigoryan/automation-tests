import pytest
import lang_massages.en.courses.index as courses_page_messages
from pages.courses.edit_page import EditPage
from tests.base_test import BaseTest


class TestEdit(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.edit_page = EditPage(browser)
        self.edit_page.click_courses_link()
        self.edit_page.click_view_course()
        # Attach self.edit_page to the class, so it can be accessed in test methods
        request.cls.edit_page = self.edit_page

    # TC0012 - Test successfully delete Course
    @pytest.mark.usefixtures("setup_class")
    def test_successfully_delete_course(self):
        self.edit_page.click_dropdown_option('Delete')
        self.edit_page.enter_delete_input('DELETE')
        self.edit_page.click_delete_course_button()
        assert self.edit_page.get_course_deleted_success_message == courses_page_messages.course_has_been_deleted
