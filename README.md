<h1 align="center">Python Packages Installation</h1>
---

## Install the packages, use pip via requirements.txt file:
```bash
pip install -r requirements.txt
```

---

## Run this command every time when install something new

```bash
pip freeze > requirements.txt
```

---

<h1 align="center">Running Tests Local</h1>
---

### Running All Tests

To run all tests, execute:

```bash
pytest
```

### Running Specific Tests

To run a specific test method, use the -k flag followed by the test method name:

```bash
pytest -k {test_some_method}
```

### Viewing Test Details

To see more running test details

- `pytest -v -s`
- `pytest -rP`
- `pytest -k {test_some_method} -rP`

---

<h1 align="center">Running Tests via GitHub</h1>
---

**The following steps are required:**

```
1. Enter the repository
2. Go to the "Actions" section
3. Enter the "Automated tests" section
4. Click on "Run workflow"
5. Select the section of tests on which we want to run the tests and give run
```

---

<h1 align="center">Documentation for automation-tests Project</h1>
---
>
> * **Lang_massages**
>   - Contains localization files for different languages, organized by language code.
> * **Locators**
>   - Contains locators for various pages, organized by functionality (e.g., authentication, courses).
> * **Pages**
>   - Contains Page Object Models (POM) for different pages, encapsulating the elements and actions on those pages.
> * **Reports**
>   - Contains directories for storing logs and screenshots generated during test execution.
>   - **logs:** Directory to store log files.
>   - **screenshots:** Directory to store screenshots taken during tests.
> * **Tests**
>   - Contains test cases organized by functionality (e.g., authentication, courses).
>   - **__init__.py:** Indicates that this directory is a Python package.
>   - **base_test.py:** Contains base test setup and teardown logic.
>   - **conftest.py:** Contains common test configurations and fixtures.
> * **Utilities**
>   - Contains utility modules for configuration, logging, and helper functions.
>   - **config.py:** Handles configuration settings for the tests.
>   - **logger.py:** Configures and initializes the logging utility.
>   - **helpers.py:** Contains helper functions used across the test suite.
> * **.github/workflows**
>   - **run_tests.yml:** Contains the GitHub Actions workflow configuration for running the test suite automatically.
> * **.env.example:** Example environment file showing required environment variables.
> * **.gitignore:** Specifies files and directories to be ignored by Git.
> * **README.md:** This file, providing an overview and documentation of the project.
> * **Requirements.txt:** Lists the Python dependencies required for the project.


### Usage functionality

##### Using logger functionality

```python
from utilities.logger import logger

logger.info('test')
logger.debug('This is a debug message')
logger.warning('This is a warning')
logger.error('This is an error message')
logger.critical('This is a critical message')
```
---




