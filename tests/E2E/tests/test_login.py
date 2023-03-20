import pytest
from selenium.webdriver.support.wait import WebDriverWait
from tests.E2E.testdata import valid_login_user, invalid_email_user, invalid_password_user
from tests.E2E.config import timeout
from tests.E2E.page_object.common_page import CommonPage
from tests.E2E.page_object.login_page import LoginPage
from tests.E2E.page_object.home_page import HomePage
from tests.E2E.page_object.login_help_page import LoginHelpPage
from tests.E2E.helpers import compare_url


def test_login_successful(driver, open_login_page):
    # Verify that user can successfully logged in with valid data
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Perform login steps: enter email, password and click on login button
    login_page.login_action(valid_login_user["username"], valid_login_user["password"])

    # Check the result: validate redirected url and validate username in left corner
    home_page.logo_name(valid_login_user["name"])
    compare_url(driver, home_page.url)


@pytest.mark.parametrize("input_text, expected_result", [([invalid_email_user["username"], invalid_password_user["password"]], invalid_email_user["message"]),
                                                         ([invalid_email_user["username"], invalid_password_user["password"]], invalid_password_user["message"])])
def test_login_invalid_credentials(driver, open_login_page, input_text, expected_result):
    # Verify that user cannot log in with invalid credentials
    login_page = LoginPage(driver)

    # Perform login with invalid credentials
    login_page.login_action(input_text[0], input_text[1])

    # Compare results in error message
    login_page.error_message_check(expected_result)


def test_need_help(driver, open_login_page):
    # Verify that user can use help link from login page
    login_page = LoginPage(driver)
    login_help_page = LoginHelpPage(driver)

    # Click on Need Help link and check that reset email field is displayed
    login_page.need_help_link.click()
    WebDriverWait(driver, timeout=timeout).until(lambda x: login_help_page.reset_email)

    # Check that user is redirected to the valid page
    compare_url(driver, login_help_page.url)


def test_need_help_from_error_message(driver, open_login_page):
    # Verify that user can use help link from error message after unsuccessful login
    login_page = LoginPage(driver)
    login_help_page = LoginHelpPage(driver)

    # Perform login with invalid credentials to get the error message
    login_page.login_action(invalid_email_user["username"], invalid_email_user["password"])
    need_help_link = login_page.need_help_link_error
    need_help_link.click()

    # Compare the existence of reset email field and correctness of the url
    WebDriverWait(driver, timeout=timeout).until(lambda x: login_help_page.reset_email)
    compare_url(driver, login_help_page.url)


def test_back_functionality(driver, open_login_page):
    # Verify that user can successfully go back to home page from login page
    login_page = LoginPage(driver)
    common_page = CommonPage(driver)
    home_page = HomePage(driver)
    login_page.go_back.click()

    # Verify that user is redirected to the previous page
    WebDriverWait(driver, timeout=timeout).until(lambda x: common_page.login)
    compare_url(driver, home_page.url)
