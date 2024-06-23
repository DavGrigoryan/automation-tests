import pytest
import lang.courses.add as add_page_messages
from pages.courses.add_page import AddPage


@pytest.mark.usefixtures("browser")
class TestAdd:

    @pytest.fixture(scope="class")
    def setup_class(self, browser, request):
        self.add_page = AddPage(browser)
        self.add_page.open()
        # Attach self.add_page to the class, so it can be accessed in test methods
        request.cls.add_page = self.add_page
        #TODO: arandznacnel open@

    # Test case for successfully add course
    @pytest.mark.usefixtures("setup_class")
    def test_successfully_add_course(self):
        self.add_page.enter_course_name('Test_1') #TODO: poxel static keyov
        self.add_page.click_save_button()
        assert self.add_page.get_course_added_success_message == add_page_messages.course_has_been_added
