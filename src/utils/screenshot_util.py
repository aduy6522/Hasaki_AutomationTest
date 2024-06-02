import os
from selenium.webdriver.remote.webdriver import WebDriver

class ScreenshotUtil:
    @staticmethod
    def take_screenshot(driver: WebDriver, file_path: str):
        driver.save_screenshot(file_path)