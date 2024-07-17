import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from utilities.config import config
from utilities.logger import logger

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def browser():
    """
    Fixture to initialize and provide a Selenium WebDriver instance.
    The browser session will be used for the entire test session and
    will be closed after all tests have been executed.
    """
    app_env = config("APP_ENV")

    if app_env == "local":
        # Initialize Chrome WebDriver for local environment
        chrome_browser = webdriver.Chrome()
    else:
        # Set Chrome options for headless execution in non-local environments
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--headless')
        chrome_browser = webdriver.Chrome(options=options)

    chrome_browser.implicitly_wait(0)
    chrome_browser.maximize_window()

    yield chrome_browser  # Provide the fixture value to the tests

    # Teardown: Quit the WebDriver session after all tests have been executed
    chrome_browser.quit()


@pytest.fixture(scope="module")
def clear_browser_cookies(browser):
    """
    Fixture to clear browser cookies before running tests in the module.
    This ensures that each test module starts with a clean session.
    If you use this: `@pytest.mark.usefixtures("clear_browser_cookies")`
    """
    # Clear all cookies
    browser.delete_all_cookies()

    def session_end():
        # Optional teardown logic if needed
        pass

    yield
    session_end()
