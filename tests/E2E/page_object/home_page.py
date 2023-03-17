from tests.E2E.locators.common_page import CommonPageLocators
from tests.E2E.locators.home_page import HomePageLocators
from tests.E2E.page_object.common_page import CommonPage


class HomePage(CommonPage):
    @property
    def url(self):
        return super(HomePage, self).url + '/home'

    def logo_name(self, name):
        return self.driver.find_elements(HomePageLocators().get_logo_name(name))
