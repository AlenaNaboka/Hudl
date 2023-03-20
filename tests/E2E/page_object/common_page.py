from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.E2E.locators.common_page import CommonPageLocators
from tests.E2E.config import base_url, timeout


class CommonPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return base_url

    @property
    def login(self):
        return WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.presence_of_element_located(CommonPageLocators.LOGIN_BUTTON)
        )

    @property
    def login_hudl(self):
        return WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.presence_of_element_located(CommonPageLocators.LOGIN_HUDL_BUTTON)
        )
