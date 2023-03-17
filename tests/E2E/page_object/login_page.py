from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.E2E.locators.login_page import LoginPageLocators
from tests.E2E.page_object.common_page import CommonPage
from tests.E2E.config import timeout


class LoginPage(CommonPage):

    @property
    def url(self):
        return super(LoginPage, self).url + '/login'

    @property
    def username(self):
        return self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)

    @property
    def password(self):
        return self.driver.find_elements(*LoginPageLocators.PASSWORD_FIELD)[0]

    @property
    def login_button(self):
        return self.driver.find_elements(*LoginPageLocators.LOGIN_BUTTON)[0]

    @property
    def login_error(self):
        return self.driver.find_elements(*LoginPageLocators.LOGIN_ERROR)[0]

    @property
    def need_help_link(self):
        return WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.presence_of_element_located(LoginPageLocators.NEED_HELP_LINK))

    @property
    def need_help_link_error(self):
        # return self.driver.find_elements(*LoginPageLocators.NEED_HELP_LINK)
        return WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.presence_of_element_located(LoginPageLocators.NEED_HELP_LINK_ERROR))

    def error_message_check(self, error_message):
        error_text = WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.presence_of_element_located(LoginPageLocators.LOGIN_ERROR)).text
        assert error_text == error_message

    def login_action(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
