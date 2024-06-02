import pytest
from selenium import webdriver
from src.pages.home_page import HomePage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    driver.get("https://hasaki.vn/")
    yield driver
    driver.quit()

def test_search_functionality(setup):
    home_page = HomePage(setup)
    home_page.enter_search_term("skincare")
    home_page.click_search_button()
    # Add assertions to verify search results