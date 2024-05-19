from selenium.webdriver.common.by import By


class BasePageLocators:
    MINIMIZE_LINK_CSS = (By.CSS_SELECTOR, "#console-size a[title='Minimize']")
