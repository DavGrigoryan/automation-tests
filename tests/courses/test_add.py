import allure
import pytest
import lang_massages.en.courses.index as courses_page_messages
from pages.courses.add_page import AddPage
from tests.base_test import BaseTest


@allure.feature('Courses tests')
@pytest.mark.usefixtures("clear_browser_cookies")
class TestAdd(BaseTest):

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.add_page = AddPage(browser)
        self.add_page.open()
        self.add_page.click_courses_link()
        self.add_page.click_add_new_course_link()
        # Attach self.add_page to the class, so it can be accessed in test methods
        request.cls.add_page = self.add_page

    @allure.story('TC0006 - Test successfully add new Course')
    @pytest.mark.usefixtures("setup_class")
    def test_successfully_add_course(self):
        self.add_page.enter_course_name(self.get_prefix('Course_1'))
        self.add_page.click_save_button()
        with allure.step('Check if course has been added successfully'):
            assert self.add_page.get_course_added_success_message == courses_page_messages.course_has_been_added
