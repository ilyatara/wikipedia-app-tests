import allure
from allure_commons.types import Severity

from wikipedia_app_tests.pages.tutorial_page import TutorialPage
from wikipedia_app_tests.utils.appium import by_id


pytestmark = [
    allure.tag('mobile'),
    allure.label('owner', 'Ilya Tarasov'),
    allure.feature('Tutorial')
]


@allure.severity(Severity.CRITICAL)
@allure.title('After skipping the tutorial the main screen opens')
def test_skip_tutorial():
    page = TutorialPage()
    page.skip()
    page.should_have_main_page_opened()


@allure.severity(Severity.NORMAL)
@allure.title('All screens of the tutorial have expected contents')
def test_tutorial_screens_contents():
    page = TutorialPage()

    with allure.step('Check elements on the 1st tutorial screen'):
        page.should_have_image()
        page.should_have_header_and_text(
            'The Free Encyclopedia',
            'We’ve found the following on your device:'
        )
        page.should_have_element_with_text(
            by_id('org.wikipedia.alpha:id/option_label'),
            'English'
        )
        page.should_have_element_with_text(
            by_id('org.wikipedia.alpha:id/addLanguageButton'),
            'Add or edit languages'
        )

    page.tap_continue()

    with allure.step('Check elements on the 2nd tutorial screen'):
        page.should_have_image()
        page.should_have_header_and_text(
            'New ways to explore',
            'Dive down the Wikipedia rabbit hole'
        )

    page.tap_continue()

    with allure.step('Check elements on the 3rd tutorial screen'):
        page.should_have_image()
        page.should_have_header_and_text(
            'Reading lists with sync',
            'You can make reading lists from articles'
        )

    page.tap_continue()

    with allure.step('Check elements on the 4th tutorial screen'):
        page.should_have_image()
        page.should_have_header_and_text(
            'Send anonymous data',
            'Help make the app better'
        )
        page.should_have_element_with_text(
            by_id('org.wikipedia.alpha:id/rejectButton'),
            'Reject'
        )
        page.should_have_element_with_text(
            by_id('org.wikipedia.alpha:id/acceptButton'),
            'Accept'
        )

    page.tap_accept()

    page.should_have_main_page_opened()
