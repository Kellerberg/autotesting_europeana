import pytest
import random
import time
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def set_browser_configuration():
    browser.config.browser_name = 'firefox'
    browser.open('https://www.europeana.eu/en')
    browser.driver.set_window_size(width=1400, height=800)
    browser.config.hold_browser_open = False


@pytest.fixture
def entering_advanced_search_form(set_browser_configuration):
    browser.element('.form-control').should(be.visible).click()
    browser.element('#search-form-options > a').should(be.visible).click()


def test_searching_from_main(set_browser_configuration):
    search_input = 'cats'
    browser.element('.form-control').should(be.visible).click().type(search_input).press_enter()
    browser.element('.col-results').should(have.no.text('0 results'))
    browser.element('.col-results').should(have.text(search_input))


def test_searching_search_for_everything(set_browser_configuration):
    browser.element('#show-search-button').click()
    browser.element('#search-form-options > a').should(be.visible).click()
    browser.element('.col-results').should(have.text('results'))


def test_searching_by_input(set_browser_configuration):
    time.sleep(1)
    search_input = 'cats'
    browser.element('#show-search-button').click()
    browser.element('.form-control').should(be.visible).type(search_input).press_enter()
    browser.element('.col-results').should(have.no.text('0 results'))
    browser.element('.col-results').should(have.text(search_input))


def test_searching_by_input_0_results(set_browser_configuration):
    time.sleep(1)
    random.seed()
    random_request = ''
    for x in range(15):
        random_request = random_request + random.choice(list('12345678909qwertyuiopasdfghjklzxcvbnm'))

    search_input = random_request
    browser.element('#show-search-button').click()
    browser.element('.form-control').should(be.visible).type(search_input).press_enter()
    browser.element('.col-results').should(have.text('0 results'))


def test_checking_advanced_search_opens(set_browser_configuration, entering_advanced_search_form):
    browser.element('.filters-title').should(have.text('Filter results'))


def test_applying_search_filters(set_browser_configuration, entering_advanced_search_form):
    time.sleep(2)
    browser.element('[data-qa="collection side facet dropdown button"]').click()
    browser.element('[data-qa="art collection field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Art'))

    browser.element('[data-qa="TYPE side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="IMAGE TYPE field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Image'))

    browser.element('[data-qa="REUSABILITY side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="open REUSABILITY field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Yes'))

    browser.element('[data-qa="COUNTRY side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="Netherlands COUNTRY field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Netherlands'))

    browser.element('[data-qa="LANGUAGE side facet dropdown button"]').click()
    browser.element('[data-qa="en LANGUAGE field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('English'))

    browser.element('[data-qa="PROVIDER side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="The European Library PROVIDER field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('The European Library'))

    browser.element('[data-qa="DATA_PROVIDER side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="National Library of the Netherlands DATA_PROVIDER field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('National Library of the Netherlands'))

    browser.element('[data-qa="COLOURPALETTE side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="#000000 COLOURPALETTE field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Black'))

    browser.element('[data-qa="IMAGE_ASPECTRATIO side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="landscape IMAGE_ASPECTRATIO field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Landscape'))

    browser.element('[data-qa="IMAGE_SIZE side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="medium IMAGE_SIZE field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Medium 0.5-1MP (e.g. 850x850px)'))

    browser.element('[data-qa="MIME_TYPE side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="image/jpeg MIME_TYPE field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('JPEG'))

    browser.element('[data-qa="RIGHTS side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="*/publicdomain/mark/* RIGHTS field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Public Domain Mark'))

    browser.element('[data-qa="contentTier side facet dropdown button"]').should(be.clickable).click()
    browser.element('[data-qa="2 contentTier field"]').should(be.clickable).click()
    time.sleep(0.5)
    browser.element('[data-qa="side filters"]').should(have.text('Medium quality'))

    browser.element('[data-qa="reset filters button"]').should(be.visible).click()
    browser.element('[data-qa="reset filters button"]').should(be.not_.visible)
