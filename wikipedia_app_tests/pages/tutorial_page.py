import allure
from selene import be, have

from wikipedia_app_tests.pages.main_page import MainPage
from wikipedia_app_tests.utils.appium import by_id


class TutorialPage:
    skip_button = by_id('org.wikipedia.alpha:id/fragment_onboarding_skip_button')
    continue_button = by_id('org.wikipedia.alpha:id/fragment_onboarding_forward_button')
    accept_button = by_id('org.wikipedia.alpha:id/acceptButton')
    image = by_id('org.wikipedia.alpha:id/imageViewCentered')
    primary_text = by_id('org.wikipedia.alpha:id/primaryTextView')
    secondary_text = by_id('org.wikipedia.alpha:id/secondaryTextView')

    def skip(self):
        with allure.step('Skip tutorial'):
            self.skip_button.click()

    def tap_continue(self):
        with allure.step('Tap the "Continue" button'):
            self.continue_button.click()

    def tap_accept(self):
        with allure.step('Tap the "Accept" button'):
            self.accept_button.click()

    def should_have_image(self):
        with allure.step('Check that image is present'):
            self.image.should(be.visible)

    def should_have_header_and_text(self, header, text):
        with allure.step('Check header and text'):
            self.primary_text.should(have.text(header))
            self.secondary_text.should(have.text(text))

    def should_have_element_with_text(self, locator, text):
        with allure.step(f'Check element\'s text: {text}'):
            locator.should(have.text((text)))

    def should_have_main_page_opened(self):
        with allure.step('Check that the main screen has opened'):
            main_page = MainPage()
            main_page.should_be_opened()
