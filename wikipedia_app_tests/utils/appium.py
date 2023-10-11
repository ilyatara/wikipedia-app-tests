from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


def by_id(value, all=False):
    if all:
        return browser.all((AppiumBy.ID, value))
    return browser.element((AppiumBy.ID, value))


def by_accessibility_id(value):
    return browser.element((AppiumBy.ACCESSIBILITY_ID, value))


def by_xpath(value):
    return browser.element((AppiumBy.XPATH, value))
