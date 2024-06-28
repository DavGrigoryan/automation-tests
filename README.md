<h1 align="center">Python Packages Installation</h1>
---

## To install the packages, use pip:

**You can choose either N_1 or N_2 from these two options:**

**N_1**
```bash
pip install selenium
pip install pytest
pip install python-dotenv
pip install python-decouple
```

**N_2**
```bash
pip install -r requirements.txt
```

---

## Run this command every time you install something new

```bash
pip freeze > requirements.txt
```

---

<h1 align="center">Running Tests</h1>
---

### Running All Tests

To run all tests, execute:

```bash
pytest
```

---

### Running Specific Tests

To run a specific test method, use the -k flag followed by the test method name:

```bash
pytest -k {test_some_method}
```

---

### Viewing Test Details

To see more running test details

- `pytest -v -s`
- `pytest -rP`
- `pytest -k {test_some_method} -rP`

---

### To run tests on Github
The following steps are required:
```

1. Enter the repository
2. Go to the "Actions" section
3. Enter the "Automated tests" section
4. Click on "Run workflow"
5. Select the section of tests on which we want to run the tests and give run
```
