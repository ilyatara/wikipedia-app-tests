import allure
from selene import have

from wikipedia_app_tests.utils.appium import by_id, by_accessibility_id, by_xpath


def test_search():

    with allure.step('Skip tutorial'):
        by_id('org.wikipedia.alpha:id/fragment_onboarding_skip_button').click()

    with allure.step('Type search request'):
        by_accessibility_id('Search Wikipedia').click()
        by_id('org.wikipedia.alpha:id/search_src_text').type('Appium')

    with allure.step('Verify the article is first in search results'):
        results = by_id('org.wikipedia.alpha:id/page_list_item_title', all=True)
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_article():

    with allure.step('Skip tutorial'):
        by_id('org.wikipedia.alpha:id/fragment_onboarding_skip_button').click()

    with allure.step('Type search request'):
        by_accessibility_id('Search Wikipedia').click()
        by_id('org.wikipedia.alpha:id/search_src_text').type('lk-99')

    with allure.step('Verify the article is first in search results'):
        results = by_id('org.wikipedia.alpha:id/page_list_item_title', all=True)
        results.should(have.size_greater_than(0))
        results.first.should(have.text('LK-99'))

    with allure.step('Open the article'):
        by_id('org.wikipedia.alpha:id/page_list_item_title', all=True).first.click()

    with allure.step('Verify the article is correct'):
        by_xpath('//android.widget.TextView[@resource-id="pcs-edit-section-title-description"]')\
            .should(have.text('Proposed superconducting material'))
