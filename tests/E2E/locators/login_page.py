from selenium.webdriver.common.by import By


class LoginPageLocators:
    # FIELDS
    USERNAME_FIELD = By.ID, 'email'
    PASSWORD_FIELD = By.ID, 'password'

    # BUTTONS
    LOGIN_BUTTON = By.ID, 'logIn'
    GO_BACK_BUTTON = By.CSS_SELECTOR, 'svg[class^="styles_backIcon"]'
    ORGANIZATION_LOGIN_BUTTON = By.CSS_SELECTOR, '[data-qa-id=log-in-with-organization-btn]'

    # LINKS
    NEED_HELP_LINK = By.CSS_SELECTOR, '[data-qa-id=need-help-link]'
    NEED_HELP_LINK_ERROR = By.XPATH, '//a[text()="Need help?"]'

    # CHECKBOXES
    REMEMBER_ME_CHECKBOX = By.CSS_SELECTOR, '[data-qa-id=remember-me-checkbox-label]'

    # TEXT
    LOGIN_ERROR = By.CSS_SELECTOR, '[data-qa-id=error-display]'
