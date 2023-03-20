from tests.E2E.page_object.login_page import LoginPage
from tests.E2E.locators.login_help_page import LoginHelpPageLocators


class LoginHelpPage(LoginPage):
    @property
    def url(self):
        return super(LoginHelpPage, self).url + '/help#'

    @property
    def reset_email(self):
        return self.driver.find_elements(*LoginHelpPageLocators.RESET_EMAIL_INPUT)[0]
