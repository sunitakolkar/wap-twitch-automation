import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging
from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage
from Config.config import TestData
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
@pytest.fixture(scope="module")
def driver():
    # Configure Chrome to emulate a mobile device
    mobile_emulation = {
            "deviceName": "iPhone 12 Pro"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(TestData.CHROME_EXECUTABLE_PATH), options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def search_results_page(driver):
    return SearchResultsPage(driver)

def test_search_starcraft_II(home_page,search_results_page):
    home_page.navigate_to(TestData.BASE_URL)
    home_page.click_search_button()
    home_page.wait_for_element(*home_page.input_search)
    home_page.enter_search_data("StarCraft II")
    time.sleep(3)
    home_page.submit_search()
    search_results_page.wait_for_element(*search_results_page.search_result_page_title)
    search_results_page.scroll_down_two_times()
    search_results_page.close_popup_modal()
    search_results_page.click_streamer_app()
    # Take a screenshot and save it to a file
    time.sleep(5) # wait until the page loads
    search_results_page.take_screenshot("streamer.png")

