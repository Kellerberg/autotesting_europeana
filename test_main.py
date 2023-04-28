import allure
from selene import be, have


@allure.title('Testing search')
def test_search(setup_browser):

    browser = setup_browser

    search = 'cats'

    with allure.step('Open main page'):
        browser.open('https://www.europeana.eu/en')
    with allure.step('Opening search box'):
        browser.element('[data-qa="show search button"]').should(be.visible).click()
    with allure.step('Input search request'):
        browser.element('[data-qa="search box"]').should(be.visible).type(search).press_enter()
    with allure.step('Checking results'):
        browser.element('[data-qa="search page"]').should(have.text(search))
