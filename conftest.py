import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from decouple import config

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def browser():
    app_env = config("APP_ENV")

    if app_env == "local":
        chrome_browser = webdriver.Chrome()
    else:
        options = Options()
        options.add_argument('--headless')
        chrome_browser = webdriver.Chrome(options=options)

    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()

    yield chrome_browser  # Provide the fixture value to the tests

    # Teardown: Quit the WebDriver session after all tests have been executed
    chrome_browser.quit()


@pytest.fixture(autouse=True)
def clear_browser_cookies(browser): 
    # Clear browser cookies before each test
    browser.delete_all_cookies()
