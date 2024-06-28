from selenium.webdriver.common.by import By
from utilities.helpers import route_app


class AddPageLocators:
    COURSES_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('courses/') + '"]')
    ADD_NEW_COURSE_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('courses/add') + '"]')
    COURSE_NAME = (By.NAME, "name")
    SAVE_BUTTON = (By.ID, "add-new-course-btn")
    COURSE_ADDED_SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
