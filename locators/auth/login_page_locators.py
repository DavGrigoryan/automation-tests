from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "Email")
    PASSWORD_INPUT = (By.NAME, "Pass")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary.w-100')
    ERROR_MESSAGE = (By.ID, "login-error-message")
    IS_LOGGED_IN = (By.CSS_SELECTOR, "a[href='https://eleapdemo.eleapdev2.com/account/']")
