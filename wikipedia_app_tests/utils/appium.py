from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


def by_id(value):
    return browser.element((AppiumBy.ID, value))
