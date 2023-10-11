import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


class MainPage:
    search_input = browser.element(
        (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))

    def should_be_opened(self):
        with allure.step('Check that the main screen is opened'):
            self.search_input.should(be.present)
