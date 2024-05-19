<h1 align="center">Python Packages Installation</h1>
---

To install the packages, use pip:

```bash
pip install selenium
```

```bash
pip install pytest
```

```bash
pip install python-dotenv
```

```bash
pip install python-decouple
```

Run this command every time you install something new

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

- `pytest -rP`
- `pytest -k {test_some_method} -rP`

---

- locators.py֊ ները առանձնացրու ու առանձին գրի ամեն էջը իր locators֊ները պետք է ունենա

- test֊երի մեջ գրված error message֊ները պետք է constant֊ներով գա

- ամեն թեստ պետք է անկախ լինի ուրիշ թեստերից