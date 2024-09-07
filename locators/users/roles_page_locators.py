from selenium.webdriver.common.by import By
from utilities.helpers import route_app


class RolesPageLocators:
    ADD_NEW_ROLE_BUTTON = (By.CSS_SELECTOR, 'button[data-target="#addNewRole"]')
    ADD_NAME_INPUT = (By.XPATH, "//form[@action='" + route_app('roles/') + "']//input[@name='name']")
    ADD_DESCRIPTION_INPUT = (By.XPATH, "//form[@action='" + route_app('roles/') + "']//textarea[@name='description']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space(text())='SAVE']")
    EDIT_BUTTON = (By.CLASS_NAME, "edit_btn")
    DELETE_BUTTON = (By.XPATH, "//button[normalize-space(text())='delete']")
