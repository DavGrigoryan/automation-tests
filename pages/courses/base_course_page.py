from pages.custom_base_page import CustomBasePage


class BaseCoursePage(CustomBasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.login_as_admin()
