from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.E2E.config import timeout
from tests.E2E.locators.common_page import CommonPageLocators
from tests.E2E.locators.home_page import HomePageLocators
from tests.E2E.page_object.common_page import CommonPage
from tests.E2E.page_object.login_page import LoginPage
from tests.E2E.locators.login_help_page import LoginHelpPageLocators


class LoginHelpPage(LoginPage):
    @property
    def url(self):
        return super(LoginHelpPage, self).url + '/help#'

    @property
    def reset_email(self):
        return self.driver.find_elements(*LoginHelpPageLocators.RESET_EMAIL_INPUT)[0]
