from selenium.webdriver.common.by import By


class IndexPageLocators:
    ADD_NEW_USER_LINK = (By.CSS_SELECTOR, 'button[data-target="#addUserModal"]')
    USER_LAST_NAME = (By.NAME, "last_name")
    USER_EMAIL = (By.NAME, "email")
    ADD_USER_BUTTON = (By.XPATH, '//button[text()="Add User"]')
