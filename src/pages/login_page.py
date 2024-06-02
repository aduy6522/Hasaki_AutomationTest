from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")

    def enter_username(self, username: str):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()