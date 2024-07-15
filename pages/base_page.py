from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from locators.auth.login_page_locators import LoginPageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def find_element(self, locator, condition=None, timeout=5):
        if condition is not None:
            wait = WebDriverWait(self.browser, timeout)
            return wait.until(condition(locator))
        else:
            return self.browser.find_element(*locator)

    def find_elements(self, locator, condition=None, timeout=5):
        if condition is not None:
            wait = WebDriverWait(self.browser, timeout)
            return wait.until(condition(locator))
        else:
            return self.browser.find_elements(*locator)

    def is_element_found(self, locator, condition=None, timeout=5):
        try:
            self.find_element(locator, condition, timeout)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def send_keys(self, locator, keys, condition=None, timeout=5):
        self.find_element(locator, condition, timeout).send_keys(keys)

    def click_element(self, locator, condition=None, timeout=5):
        self.find_element(locator, condition, timeout).click()

    def clear_input(self, locator, condition=None, timeout=5):
        self.find_element(locator, condition, timeout).clear()

    def wait_for_condition(self, locator, condition, timeout=5):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(lambda driver: condition(self.find_element(locator)))

    def wait_for_element(self, locator, condition, timeout=5):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(condition(locator))

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator, condition=None, timeout=5):
        element = self.find_element(locator, condition, timeout)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()  # Scroll to the element

    def scroll_by_amount(self, x, y):
        self.browser.execute_script(f"window.scrollBy({x}, {y});")

    # ---------- Custom basic functions ----------

    def click_login_button(self):
        self.click_element(LoginPageLocators.SIGN_IN_BUTTON)

    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
