import logging


def compare_url(driver, expected_url):
    current_url = driver.current_url
    logging.info("Current URL: ", current_url)
    logging.info("Expected URL: ", expected_url)
    assert current_url == expected_url
