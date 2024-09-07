from selenium.webdriver.common.by import By

from utilities.helpers import route_app


class IndexPageLocators:
    ADD_NEW_USER_LINK = (By.CSS_SELECTOR, 'button[data-target="#addUserModal"]')
    USER_TITLE = (By.NAME, "title")
    USER_FIRST_NAME = (By.NAME, "first_name")
    USER_LAST_NAME = (By.NAME, "last_name")
    USER_EMAIL = (By.NAME, "email")
    USER_ACCESS_LEVEL = (By.NAME, "id_acl_role")
    ADD_USER_BUTTON = (By.XPATH, '//button[text()="Add User"]')
    CHECK_ALL_CHECKBOX = (By.CSS_SELECTOR, "#es_automation_users-table .check-all")
    DELETE_SELECTED_USERS = (By.ID, "trigger-delete")
    USERS_TABLE = (By.ID, "es_automation_users-table")
    USER_NAME_LINK = (By.CSS_SELECTOR, "a.text-nowrap")
    WIZARD_STEPS = (By.ID, "wizard-steps")
    TABLE_INFO_OF_USER = (By.CLASS_NAME, "table_info_of_user")
    SAVE_CHANGES_BUTTON = (By.XPATH, "//button[normalize-space(text())='Save']")
    SUB_MENU_USERS_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('users/') + '"]')
    SUB_MENU_CUSTOM_FIELDS_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('users/custom_fields') + '"]')
    SUB_MENU_ROLES_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('roles/') + '"]')
    SUB_MENU_USER_GROUPS_LINK = (By.CSS_SELECTOR, 'a[href="' + route_app('user_groups/') + '"]')
