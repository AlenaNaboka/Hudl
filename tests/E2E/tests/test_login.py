import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.E2E.testdata import valid_login_user, invalid_email_user, invalid_password_user
from tests.E2E.config import timeout
from tests.E2E.page_object.common_page import CommonPage
from tests.E2E.page_object.login_page import LoginPage
from tests.E2E.page_object.home_page import HomePage
from tests.E2E.page_object.login_help_page import LoginHelpPage


def test_login_successful():
    driver = webdriver.Chrome('../chromedriver')
    common_page = CommonPage(driver)
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    driver.get(common_page.url)
    driver.maximize_window()

    common_page.login.click()
    login_hudl = WebDriverWait(driver, timeout=10).until(lambda x: common_page.login_hudl)
    login_hudl.click()

    login_username = WebDriverWait(driver, timeout=10).until(lambda x: login_page.username)
    login_password = WebDriverWait(driver, timeout=10).until(lambda x: login_page.password)
    login_username.send_keys(valid_login_user["username"])
    login_password.send_keys(valid_login_user["password"])

    login_page.login_button.click()

    # name_logo = WebDriverWait(driver, timeout=10).until(lambda x: home_page.logo_name(valid_login_user["name"]))
    name_logo = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                                 f"//span[text()=\"{valid_login_user['name']}\"]")))
    print("name_logo:", name_logo)

    current_url = driver.current_url
    print("current url: ", current_url)

    assert current_url == home_page.url

    driver.quit()


@pytest.mark.parametrize("input_text, expected_result", [([invalid_email_user["username"], invalid_password_user["password"]], invalid_email_user["message"]),
                                                         ([invalid_email_user["username"], invalid_password_user["password"]], invalid_password_user["message"])])
def test_login_invalid_credentials(input_text, expected_result):
    driver = webdriver.Chrome('../chromedriver')
    common_page = CommonPage(driver)
    login_page = LoginPage(driver)
    driver.get(common_page.url)
    driver.maximize_window()

    common_page.login.click()
    login_hudl = WebDriverWait(driver, timeout=10).until(lambda x: common_page.login_hudl)
    login_hudl.click()

    login_page.login_action(input_text[0], input_text[1])
    login_page.error_message_check(expected_result)

    driver.quit()


def test_need_help():
    driver = webdriver.Chrome('../chromedriver')
    common_page = CommonPage(driver)
    login_page = LoginPage(driver)
    login_help_page = LoginHelpPage(driver)

    driver.get(common_page.url)
    driver.maximize_window()

    common_page.login.click()
    login_hudl = WebDriverWait(driver, timeout=timeout).until(lambda x: common_page.login_hudl)
    login_hudl.click()

    login_page.need_help_link.click()

    WebDriverWait(driver, timeout=timeout).until(lambda x: login_help_page.reset_email)

    current_url = driver.current_url

    assert current_url == login_help_page.url

    driver.quit()


def test_need_help_from_error_message():
    driver = webdriver.Chrome('../chromedriver')
    common_page = CommonPage(driver)
    login_page = LoginPage(driver)
    login_help_page = LoginHelpPage(driver)

    driver.get(common_page.url)
    driver.maximize_window()

    common_page.login.click()
    login_hudl = WebDriverWait(driver, timeout=timeout).until(lambda x: common_page.login_hudl)
    login_hudl.click()

    login_page.login_action(invalid_email_user["username"], invalid_email_user["password"])
    need_help_link = login_page.need_help_link_error
    need_help_link.click()

    WebDriverWait(driver, timeout=timeout).until(lambda x: login_help_page.reset_email)

    current_url = driver.current_url

    assert current_url == login_help_page.url

    driver.quit()


def test_login_with_organization():
    pass


def test_back_functionality():
    pass
