from selenium.webdriver.common.by import By
from utilities.helpers import route_app


class UserGroupsPageLocators:
    ADD_NEW_USER_GROUP_LINK = (By.CSS_SELECTOR, 'button[data-target="#userGroupModal"]')
    USER_GROUP_NAME_INPUT = (By.XPATH, "//form[@action='" + route_app('user_groups/') + "']//input[@name='name']")
    USER_GROUP_DESCRIPTION_INPUT = \
        (By.XPATH, "//form[@action='" + route_app('user_groups/') + "']//textarea[@name='description']")
    ADD_USER_GROUP_BUTTON = (By.ID, "save-group-btn")
    EDIT_BUTTON = (By.XPATH, ".//a[contains(@href, 'user_groups/edit') and text()='edit']")
    EDIT_NAME_INPUT = (By.XPATH, "//form[@id='new-group-form']//input[@name='name']")
    EDIT_DESCRIPTION_INPUT = (By.XPATH, "//form[@id='new-group-form']//textarea[@name='description']")
    DELETE_BUTTON = (By.XPATH, ".//a[contains(@href, 'user_groups/delete') and text()='delete']")
    TABLE_USER_GROUPS = (By.CSS_SELECTOR, "div.table-responsive")
