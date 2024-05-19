import pytest
from selenium import webdriver
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()

    yield chrome_browser  # Provide the fixture value to the tests

    # Teardown: Quit the WebDriver session after all tests have been executed
    chrome_browser.quit()


@pytest.fixture(autouse=True)
def clear_browser_cookies(browser): 
    # Clear browser cookies before each test
    browser.delete_all_cookies()
