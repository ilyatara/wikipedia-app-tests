from wikipedia_app_tests.pages.search_page import SearchPage


def test_find_article():
    page = SearchPage()
    page.type_search_request('appium')
    page.should_have_first_search_result_title('Appium')


def test_open_article():
    page = SearchPage()
    page.type_search_request('lk-99')
    page.should_have_first_search_result_title(('LK-99'))
    page.open_search_result(index=0)
    page.should_have_opened_article_with_subtitle('Proposed superconducting material')
