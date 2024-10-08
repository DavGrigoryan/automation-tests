from selenium.webdriver.common.by import By


class BasePageLocators:
    TAG_A = (By.TAG_NAME, 'a')
    TAG_TR = (By.TAG_NAME, 'tr')
    TAG_TD = (By.TAG_NAME, 'td')
    MINIMIZE_LINK_CSS = (By.CSS_SELECTOR, "#console-size a[title='Minimize']")
    ALERT_SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    ALERT_DANGER_MESSAGE = (By.CLASS_NAME, "alert-danger")
    HEADER_MENU_DASHBOARD_LINK = (By.ID, 'es_automation_header_menu_index')
    HEADER_MENU_COURSES_LINK = (By.ID, 'es_automation_header_menu_courses')
    HEADER_MENU_LEARNING_PATHS_LINK = (By.ID, 'es_automation_header_menu_career_paths')
    HEADER_MENU_SKILLS_LINK = (By.ID, 'es_automation_header_menu_skills')
    HEADER_MENU_CREDENTIALS_LINK = (By.ID, 'es_automation_header_menu_ce')
    HEADER_MENU_OJT_LINK = (By.ID, 'es_automation_header_menu_ojt')
    HEADER_MENU_USERS_LINK = (By.ID, 'es_automation_header_menu_users')
    HEADER_MENU_REPORTS_LINK = (By.ID, 'es_automation_header_menu_reports')
    HEADER_MENU_ECOMMERCE_LINK = (By.ID, 'es_automation_header_menu_ecommerce')
    FILTER_SEARCH_BY_NAME_OR_EMAIL = (By.XPATH, "//input[@placeholder='Search by Name or Email']")
    FILTER_APPLY_FILTERS_BUTTON = (By.XPATH, "//button[@type='submit' and contains(translate(text(), "
                                             "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
                                             "'apply filters')]")
