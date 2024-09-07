import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def find_element(self, locator, condition=None, timeout: int = 10):
        try:
            if condition is not None:
                wait = WebDriverWait(self.browser, timeout)
                return wait.until(condition(locator))
            else:
                return self.browser.find_element(*locator)
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.")

    def find_elements(self, locator, condition=None, timeout: int = 10):
        if condition is not None:
            wait = WebDriverWait(self.browser, timeout)
            return wait.until(condition(locator))
        else:
            return self.browser.find_elements(*locator)

    def find_child_element(self, parent_element, locator, condition=None, timeout: int = 10):
        try:
            if condition is not None:
                wait = WebDriverWait(self.browser, timeout)
                return wait.until(lambda driver: condition(parent_element.find_element(*locator)))
            else:
                return parent_element.find_element(*locator)
        except TimeoutException:
            raise TimeoutException(f"Child element with locator {locator} not found within {timeout} seconds.")

    def find_child_elements(self, parent_element, locator, condition=None, timeout: int = 10):
        try:
            if condition is not None:
                wait = WebDriverWait(self.browser, timeout)
                return wait.until(lambda driver: condition(parent_element.find_elements(*locator)))
            else:
                return parent_element.find_elements(*locator)
        except TimeoutException:
            raise TimeoutException(f"Child element with locator {locator} not found within {timeout} seconds.")

    def is_element_found(self, locator, condition=None, timeout: int = 10):
        try:
            self.find_element(locator, condition, timeout)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def send_keys(self, locator, keys, condition=None, timeout: int = 10):
        self.find_element(locator, condition, timeout).send_keys(keys)

    def click_element(self, locator, condition=None, timeout: int = 10):
        self.find_element(locator, condition, timeout).click()

    def clear_input(self, locator, condition=None, timeout: int = 10):
        self.find_element(locator, condition, timeout).clear()

    def select_option(self, locator, option_value=None, option_text=None, option_index=None,
                      condition=None, timeout: int = 10):
        dropdown_element = self.find_element(locator, condition, timeout)
        select = Select(dropdown_element)

        if option_value is not None:
            select.select_by_value(option_value)
        elif option_text is not None:
            select.select_by_visible_text(option_text)
        elif option_index is not None:
            select.select_by_index(option_index)

    def wait_for_condition(self, locator, condition, timeout: int = 10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(lambda driver: condition(self.find_element(locator)))

    def wait_for_dom_to_load(self, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_for_element(self, locator, condition, timeout: int = 10):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(condition(locator))

    def scroll_to_bottom(self, timeout: int = 10):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait until the page is fully scrolled to the bottom
        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.execute_script("return window.innerHeight + window.scrollY >= "
                                                 "document.body.scrollHeight")
        )

    def scroll_to_element(self, locator, condition=None, timeout: int = 10):
        element = self.find_element(locator, condition, timeout)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()  # Scroll to the element

    def scroll_by_amount(self, x: int, y: int):
        self.browser.execute_script(f"window.scrollBy({x}, {y});")

    def refresh_page(self):
        self.browser.refresh()

    def alert_handler(self, action: str):
        with allure.step(f'{action.capitalize()} the alert'):
            alert = self.browser.switch_to.alert
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            else:
                raise ValueError("Invalid action. Use 'accept' or 'dismiss'.")
