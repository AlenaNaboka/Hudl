from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = By.ID, 'email'
    PASSWORD_FIELD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'logIn'
    LOGIN_ERROR = By.CSS_SELECTOR, '[data-qa-id=error-display]'
    GO_BACK_BUTTON = By.CSS_SELECTOR, '[data-qa-id=go-back]'
    REMEMBER_ME_CHECKBOX = By.CSS_SELECTOR, '[data-qa-id=remember-me-checkbox-label]'
    NEED_HELP_LINK = By.CSS_SELECTOR, '[data-qa-id=need-help-link]'
    NEED_HELP_LINK_ERROR = By.XPATH, '//a[text()="Need help?"]'
