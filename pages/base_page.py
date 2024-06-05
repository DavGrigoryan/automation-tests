import os
import importlib.util
from src.env import config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException


# need check and remove helpers folder
def route_app(url) -> str:
    return config('SUBDOMAIN') + '.' + config('APP_URL') + url


def load_module(module_name, module_path):
    path = os.path.join(module_path, module_name)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
