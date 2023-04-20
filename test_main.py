import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture

def set_browser_configuration():
    browser.config.browser_name = 'firefox'
    browser.open('https://www.europeana.eu/en')
    browser.driver.set_window_size(width=1024, height=768)
    browser.config.hold_browser_open = True


def test_search(set_browser_configuration):
    browser.element('#show-search-button').click()
    browser.element('#search-form-options > a').should(be.visible).click()
