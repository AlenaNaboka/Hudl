from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.E2E.config import timeout
from tests.E2E.locators.home_page import HomePageLocators
from tests.E2E.page_object.common_page import CommonPage


class HomePage(CommonPage):
    @property
    def url(self):
        return super(HomePage, self).url + '/home'

    def logo_name(self, name):
        return WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.presence_of_element_located(HomePageLocators().logo_name(name))
        )
