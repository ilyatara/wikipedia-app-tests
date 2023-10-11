import allure
from selene import be

from wikipedia_app_tests.utils.appium import by_accessibility_id


class MainPage:
    pseudo_search_input = by_accessibility_id('Search Wikipedia')

    def should_be_opened(self):
        with allure.step('Check that search input is visible'):
            self.pseudo_search_input.should(be.visible)

    def open_search_page(self):
        with allure.step('Tap on the main page search input'):
            self.pseudo_search_input.click()
