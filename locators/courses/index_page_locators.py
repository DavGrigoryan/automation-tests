from selenium.webdriver.common.by import By
from utilities.helpers import route_app


class IndexPageLocators:
    ADD_NEW_COURSE_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('courses/add') + '"]')
    COURSE_NAME = (By.NAME, "name")
    SAVE_BUTTON = (By.ID, "add-new-course-btn")
    COURSE_TABLE = (By.ID, 'es_automation_courses-table')
    DELETE_COURSE_BTN = (By.CLASS_NAME, 'delete_course_btn')
    DELETE_VERIFY_FIELD = (By.CLASS_NAME, "delete_verify_field")
    COURSE_NAME_LINK = (By.CSS_SELECTOR, 'a.es_automation_course_name')
    DROPDOWN_TOGGLE = (By.CLASS_NAME, 'ui-dropdown-toggle')
    DROPDOWN_ITEMS = (By.TAG_NAME, 'a')

    @staticmethod
    def dropdown_option(item_text):
        return By.XPATH, f".//li[a[contains(text(), '{item_text}')]]"
