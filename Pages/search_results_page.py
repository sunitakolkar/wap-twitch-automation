import time

from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(BasePage):
    streamer = (By.XPATH, "//h2[@title='Pajama Stream - Day 7']")
    popup = (By.XPATH, "//button[@data-a-target='modalClose']")
    search_result_page_title = (By.XPATH,"//h1[contains(.,'StarCraft II')]")
    driver = None

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def click_streamer(self, *elements):
        self.click_element(*self.streamer)

    def scroll_down_two_times(self):
        self.scroll_down(2)

    def is_element_in_viewport(self, element):
        return self.driver.execute_script("""
            function isElementInViewport(el) {
                var rect = el.getBoundingClientRect();
                return (
                    rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                );
            }
            return isElementInViewport(arguments[0]);
        """, element)
    def get_first_visible_item_from_list(self):
        try:
            # Wait for the parent list to be present
            parent_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='list']"))
            )

            # Get all child elements of the parent list
            child_elements = parent_list.find_elements(By.XPATH, "./*")

            # Iterate through child elements and find the first visible one

            for element in child_elements:
                if self.is_element_in_viewport(element):
                    print("Found visible element")
                    return element

            print("No visible element found")
            return None  # Return None if no visible element is found

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    def click_streamer_app(self):
        visible_item = self.get_first_visible_item_from_list()
        if visible_item:
            # Perform an action on the visible item, e.g., click
            visible_item.click()
            print("Clicked on the visible item")
        else:
            print("No visible item to click")
        
    def close_popup_modal(self):
        time.sleep(5)
        self.close_popup(*self.popup)
