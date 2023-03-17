from selenium.webdriver.common.by import By


class HomePageLocators:
    def get_logo_name(self, name):
        return By.XPATH, f"//span[text()='{name}']]"
