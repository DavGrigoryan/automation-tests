from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    I_CANNOT_ACCESS_MY_ACCOUNT_LINK = (By.CLASS_NAME, 'password-forgot-link')
    EMAIL_INPUT = (By.CSS_SELECTOR, "#forget input[name='email']")
    SEND_EMAIL_BUTTON = (By.XPATH, "//button[text()='Send email']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#forget div.alert.alert-danger")
