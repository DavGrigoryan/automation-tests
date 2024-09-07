import allure
import pytest
import lang_massages.en.courses.index as courses_page_messages
from pages.courses.edit_page import EditPage
from tests.base_test import BaseTest


@allure.feature('Courses tests')
class TestEditCourse(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.edit_page = EditPage(browser)
        self.edit_page.click_header_menu_courses_link()
        self.edit_page.click_first_course_in_table()
        request.cls.edit_page = self.edit_page

    @allure.story('TC0012: Test successfully delete Course')
    @pytest.mark.usefixtures("setup_class")
    def test_successfully_delete_course(self):
        self.edit_page.click_dropdown_option('Delete')
        self.edit_page.enter_delete_input('DELETE')
        self.edit_page.click_delete_course_button()
        with allure.step('Check if course has been deleted successfully'):
            assert self.edit_page.get_success_message == courses_page_messages.course_has_been_deleted
