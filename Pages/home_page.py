from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    search_button = (By.XPATH, "//a[@href='/search']")
    input_search = (By.XPATH, "//input[@type='search']")
    select_search_text = (By.XPATH, "//p[@class='CoreText-sc-1txzju1-0 bqCGPR']")


    def __init__(self, driver):
        super().__init__(driver)

    def click_search_button(self):
        self.click_element(*self.search_button)

    def enter_search_data(self, data):
        self.send_keys(*self.input_search, data)

    def submit_search(self):
        self.click_element(*self.select_search_text)





