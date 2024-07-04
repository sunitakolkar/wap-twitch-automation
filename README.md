Twitch Mobile Search Automation
This project contains Selenium WebDriver tests to automate the search functionality on the mobile version of the Twitch website. The tests are written in Python and use the pytest framework for test execution.

Table of Contents
Prerequisites
Installation
Project Structure
Running the Tests
Writing Tests

Installation
Clone the repository:
git clone https://github.com/yourusername/twitch-mobile-search-automation.git
cd twitch-mobile-search-automation

Install the required packages:
pip install -r requirements.txt

Project Structure
├──BasePage.py
├── home_page.py
├── search_results_page.py
├── test_Twitch.py
├── requirements.txt
└── README.md
base_page.py: Contains the base page class with common methods.
home_page.py: Contains methods specific to the home page of the Twitch mobile site.
search_results_page.py: Contains methods specific to the search results page.
test_Twitch.py: Contains the test cases.
requirements.txt: Lists the project dependencies.
README.md: This file.

Running the Tests
To run the tests, use the following command:
pytest test_Twitch.py