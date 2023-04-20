import pytest
import random
from selene.support.shared import browser
from selene import be, have

random.seed


@pytest.fixture

def set_browser_configuration():
    browser.config.browser_name = 'firefox'
    browser.open('https://www.europeana.eu/en')
    browser.driver.set_window_size(width=1280, height=1024)
    browser.config.hold_browser_open = True


def test_search_search_for_everything(set_browser_configuration):
    browser.element('#show-search-button').click()
    browser.element('#search-form-options > a').should(be.visible).click()
    browser.element('.col-results').should(have.text('results'))

def test_search_input(set_browser_configuration):
    search_input = 'cats'
    browser.element('#show-search-button').click()
    browser.element('#__BVID__197').should(be.visible).type(search_input).press_enter()
    browser.element('.col-results').should(have.text(search_input))

def test_search_input_nagative(set_browser_configuration):
    random_request = ''
    for x in range(13):
        random_request = random_request + random.choice(list('12345678909qwertyuiopasdfghjklzxcvbnm'))

    search_input = random_request
    browser.element('#show-search-button').click()
    browser.element('#__BVID__197').should(be.visible).type(search_input).press_enter()
    browser.element('.col-results').should(have.text('0 results'))
