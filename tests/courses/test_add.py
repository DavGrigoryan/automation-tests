import pytest
import lang.courses.add as add_page_messages
from pages.courses.add_page import AddPage


@pytest.mark.usefixtures("browser")
class TestAdd:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.add_page = AddPage(browser)
        self.add_page.open()

    # Test case for successfully add course
    def test_successfully_add_course(self):
        self.add_page.enter_course_name('Test_1')
        self.add_page.click_save_button()
        assert self.add_page.get_course_added_success_message == add_page_messages.course_has_been_added
