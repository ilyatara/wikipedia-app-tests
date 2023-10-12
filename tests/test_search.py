import allure
from allure_commons.types import Severity

from wikipedia_app_tests.pages.search_page import SearchPage


@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Ilya Tarasov')
@allure.feature('Search')
@allure.title('Find article by exact title')
def test_find_article_by_exact_title():
    page = SearchPage()
    page.type_search_request('appium')
    page.should_have_first_search_result_title('Appium')


@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Ilya Tarasov')
@allure.feature('Search')
@allure.title('Tap on the search result opens the correct article')
def test_open_article_from_search_results():
    page = SearchPage()
    page.type_search_request('lk-99')
    page.should_have_first_search_result_title(('LK-99'))
    page.open_search_result(index=0)
    page.should_have_opened_article_with_subtitle('Proposed superconducting material')
