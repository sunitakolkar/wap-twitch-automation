# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def navigate_to(self, url):
#         self.driver.get(url)
#
#     def find_element(self, by, value):
#         return self.driver.find_element(by, value)
#
#     def click_element(self, by, value):
#         element = self.wait_for_element(by, value)
#         element.click()
#
#     def send_keys(self, by, value, keys):
#         element = self.wait_for_element(by, value)
#         element.send_keys(keys)
#
#     def wait_for_element(self, by, value):
#         return self.wait.until(EC.presence_of_element_located((by, value)))
#
#     def take_screenshot(self, file_path):
#         self.driver.save_screenshot(file_path)
#
#     def scroll_down(self, times=2):
#         for _ in range(times):
#             self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
#
#     def close_popup_if_displayed(self, by, value):
#         try:
#             popup = self.wait.until(EC.presence_of_element_located((by, value)))
#             if popup:
#                 popup.click()
#         except TimeoutException:
#             pass  # Popup not displayed

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver= driver
        self.wait = WebDriverWait(driver,10)

    def navigate_to(self,url):
        self.driver.get(url)

    def find_element(self,by,value):
        return self.driver.find_element(by,value)

    def click_element(self,by,value):
        element = self.find_element(by, value)
        element.click()
        #WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by, value, keys):
        element = self.find_element(by, value)
        element.send_keys(keys)
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def get_title(self,title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def close_popup(self, by, value):
        try:
            popup = self.find_element(by, value)
            popup.click()
        except Exception as e:
            print(f"Popup not found or could not be closed: {e}")

    def scroll_down(self, times=2):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")

    def quit(self):
        self.driver.quit()


