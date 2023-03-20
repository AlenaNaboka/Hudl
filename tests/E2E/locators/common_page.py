from selenium.webdriver.common.by import By


class CommonPageLocators:
    # BUTTONS
    LOGIN_BUTTON = By.CSS_SELECTOR, '[data-qa-id=login-select]'
    LOGIN_HUDL_BUTTON = By.CSS_SELECTOR, '[data-qa-id=login-hudl]'
