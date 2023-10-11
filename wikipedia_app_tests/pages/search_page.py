import allure
from selene import have

from wikipedia_app_tests.pages.tutorial_page import TutorialPage, MainPage
from wikipedia_app_tests.utils.appium import by_id, by_accessibility_id, by_xpath


class SearchPage:
    pseudo_search_input = by_accessibility_id('Search Wikipedia')
    search_input = by_id('org.wikipedia.alpha:id/search_src_text')
    search_results = by_id('org.wikipedia.alpha:id/page_list_item_title', all=True)

    def type_search_request(self, value):
        TutorialPage().skip()
        MainPage().open_search_page()
        with allure.step(f'Type search request: {value}'):
            self.search_input.type(value)

    def should_have_first_search_result_title(self, value):
        with allure.step(f'Check that article with title {value} is first in search results'):
            self.search_results.first.should(have.exact_text((value)))

    def open_search_result(self, index=0):
        with allure.step('Open the first article in search results'):
            self.search_results.first.click()

    def should_have_opened_article_with_subtitle(self, value):
        with allure.step('Check that the article has expected subtitle'):
            by_xpath('//android.widget.TextView[@resource-id="pcs-edit-section-title-description"]')\
                .should(have.exact_text(value))
