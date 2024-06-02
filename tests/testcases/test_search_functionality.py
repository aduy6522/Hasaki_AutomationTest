import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import pytest
from selenium import webdriver
from src.pages.home_page import HomePage
from src.utils.screenshot_util import ScreenshotUtil

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Edge(executable_path="D:/QC_Selenium/edgedriver_win64/msedgedriver.exe")
    driver.get("https://hasaki.vn/")
    yield driver
    driver.quit()

def test_search_functionality(setup):
    home_page = HomePage(setup)
    home_page.enter_search_term("skincare")
    home_page.click_search_button()
    assert "skincare" in setup.title  # Example assertion to verify the search results page title
    ScreenshotUtil.take_screenshot(setup, os.path.join("reports", "search_functionality.png"))