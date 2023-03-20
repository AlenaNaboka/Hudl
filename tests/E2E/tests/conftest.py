import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.E2E.config import timeout, base_url
from tests.E2E.page_object.common_page import CommonPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome('../chromedriver')
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(driver):
    common_page = CommonPage(driver)
    common_page.login.click()
    login_hudl = WebDriverWait(driver, timeout=timeout).until(lambda x: common_page.login_hudl)
    login_hudl.click()
