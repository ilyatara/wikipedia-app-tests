import allure
from selene import browser, be, have
from appium.webdriver.common.appiumby import AppiumBy


def test_skip_tutorial():

    with allure.step('Skip tutorial'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()


    with allure.step('Check that the main screen has opened'):

        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        ).should(be.present)


def test_tutorial_screens_contents():

    with allure.step('Check elements on the 1st tutorial screen'):

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/imageViewCentered')
        ).should(be.present)

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.text('The Free Encyclopedia'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
        ).should(have.exact_text('We’ve found the following on your device:'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/option_label')
        ).should(have.text('English'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/addLanguageButton')
        ).should(have.exact_text('Add or edit languages'))


    with allure.step('Tap the "Continue" button'):

        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()


    with allure.step('Check elements on the 2nd tutorial screen'):

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/imageViewCentered')
        ).should(be.present)

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.exact_text('New ways to explore'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
        ).should(have.text('Dive down the Wikipedia rabbit hole'))


    with allure.step('Tap "Continue" button'):

        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()


    with allure.step('Check elements on the 3rd tutorial screen'):

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/imageViewCentered')
        ).should(be.present)

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.exact_text('Reading lists with sync'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
        ).should(have.text('You can make reading lists from articles'))


    with allure.step('Tap the "Continue" button'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
        ).click()


    with allure.step('Check elements on the 4th tutorial screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/imageViewCentered')
        ).should(be.present)

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
        ).should(have.exact_text('Send anonymous data'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
        ).should(have.text('Help make the app better'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/rejectButton')
        ).should(have.exact_text('Reject'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')
        ).should(have.exact_text('Accept'))


    with allure.step('Tap the "Accept" button'):

        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')
        ).click()


    with allure.step('Check that the main screen has opened'):

        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        ).should(be.present)
