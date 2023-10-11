import os

import pytest
import allure
import allure_commons
import requests
from selene import browser, support
from appium import webdriver
from appium.options.android import UiAutomator2Options

import project
import utils


@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            project.config.remote_url,
            options=project.config.to_driver_options()
        )

    browser.config.timeout = project.config.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.allure.attach_screenshot(browser)

    utils.allure.attach_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if project.config.context == 'bstack':
        utils.allure.attach_bstack_video(session_id)
