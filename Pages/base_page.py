from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()

    def send_keys(self, by, value, keys):
        element = self.wait_for_element(by, value)
        element.send_keys(keys)

    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def scroll_down(self, times=2):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")

    def close_popup_if_displayed(self, by, value):
        try:
            popup = self.wait.until(EC.presence_of_element_located((by, value)))
            if popup:
                popup.click()
        except TimeoutException:
            pass  # Popup not displayed
