import allure
from selene import have

from wikipedia_app_tests.utils.appium import by_xpath


class ArticlePage:
    subtitle = by_xpath('//android.widget.TextView'
                        '[@resource-id="pcs-edit-section-title-description"]')

    def should_have_subtitle(self, value):
        with allure.step(f'Check that the article has expected subtitle'):
            self.subtitle.should(have.exact_text(value))
