import allure
from selene import be

from wikipedia_app_tests.utils.appium import by_accessibility_id


class MainPage:
    search_input = by_accessibility_id('Search Wikipedia')

    def should_be_opened(self):
        with allure.step('Check that the main screen is opened'):
            self.search_input.should(be.present)
