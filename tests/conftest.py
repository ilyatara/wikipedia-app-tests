import pytest
import allure_commons
from selene import browser, support
from appium import webdriver

import project
from wikipedia_app_tests.utils import allure


@pytest.fixture(scope='function', autouse=True)
def mobile_management():

    browser.config.driver = webdriver.Remote(
        project.config.remote_url,
        options=project.config.to_driver_options()
    )

    browser.config.timeout = project.config.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach_screenshot(browser)

    allure.attach_xml(browser)

    session_id = browser.driver.session_id

    browser.quit()

    if project.config.context == 'bstack':
        allure.attach_bstack_video(session_id)
