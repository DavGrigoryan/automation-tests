from selenium.webdriver.common.by import By
from utilities.helpers import route_app


class CustomFieldsPageLocators:
    ADD_NEW_FIELD_BUTTON = (By.CSS_SELECTOR, 'button[data-target="#addNewField"]')
    FIELD_NAME_INPUT = (By.XPATH, "//form[@action='" + route_app('users/custom_fields') + "']//input[@name='name']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space(text())='SAVE']")
    EDIT_BUTTON = (By.CLASS_NAME, "edit_btn")
    DELETE_BUTTON = (By.XPATH, "//button[normalize-space(text())='delete']")
