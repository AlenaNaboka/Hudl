from tests.E2E.locators.common_page import CommonPageLocators
from tests.E2E.config import base_url


class CommonPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return base_url

    @property
    def login(self):
        return self.driver.find_element(*CommonPageLocators.LOGIN_BUTTON)

    @property
    def login_hudl(self):
        return self.driver.find_element(*CommonPageLocators.LOGIN_HUDL_BUTTON)
