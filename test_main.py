import allure
import random
from selene.support.shared import browser
from selene import be, have
import pytest
from selenium import webdriver

main_page = 'https://www.europeana.eu/en'


@allure.title('Open main page')
def test_open_main_page(setup_browser, main_page):
    browser = setup_browser

    with allure.step('Open main page'):
        browser.open(main_page)

"""
@allure.step("Open main page.")
def open_main_page():
    browser.open('https://www.europeana.eu/en')


@allure.step("Entering search request.")
def enter_search_request(search):
    browser.element('[data-qa="search box"]').should(be.visible).click().type(search).press_enter()


@allure.step("Checking search results.")
def checking_search_results(search):
    browser.element('[data-qa="search page"]').should(have.text(search))

@allure.step("Show search button.")
def show_search_button():
    browser.element('[data-qa="show search button"]').click()

@allure.step("Searching for everything.")
def searching_for_everything():
    show_search_button()
    browser.element('[data-qa="search entire collection button"]').should(be.visible).click()

@allure.step("Quick search.")
def quick_search(search):
    open_main_page()
    show_search_button()
    enter_search_request(search)


def test_searching_from_main(driver, search='cats'):
    quick_search(search)
    checking_search_results(search)


def test_searching_search_for_everything(driver, search='results'):
    open_main_page()
    searching_for_everything()
    checking_search_results(search)


def test_searching_by_input(driver, search='dogs'):
    quick_search(search)
    checking_search_results(search)
    browser.element('[data-qa="search page"]').should(have.no.text('0 results'))


def test_searching_by_input_0_results(driver):
    random.seed()
    random_request = ''
    for x in range(15):
        random_request = random_request + random.choice(list('12345678909qwertyuiopasdfghjklzxcvbnm'))

    search = random_request
    open_main_page()
    show_search_button()
    enter_search_request(search)
    search = '0 results'
    checking_search_results(search)


def test_checking_advanced_search_opens(driver):
    open_main_page()
    searching_for_everything()
    browser.element('[data-qa="side filters"]').should(have.text('Filter results'))
"""
"""
def test_applying_search_filters(set_browser_configuration):
    open_main_page()
    searching_for_everything()
    time.sleep(2)
    with allure.step("Picking THEME."):
        browser.element('[data-qa="collection side facet dropdown button"]').click()
        browser.element('[data-qa="art collection field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Art'))

    with allure.step("Picking TYPE."):
        browser.element('[data-qa="TYPE side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="IMAGE TYPE field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Image'))

    with allure.step("Picking REUSABILITY."):
        browser.element('[data-qa="REUSABILITY side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="open REUSABILITY field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Yes'))

    with allure.step("Picking COUNTRY."):
        browser.element('[data-qa="COUNTRY side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="Netherlands COUNTRY field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Netherlands'))

    with allure.step("Picking LENGUAGE."):
        browser.element('[data-qa="LANGUAGE side facet dropdown button"]').click()
        browser.element('[data-qa="en LANGUAGE field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('English'))

    with allure.step("Picking PROVIDER."):
        browser.element('[data-qa="PROVIDER side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="The European Library PROVIDER field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('The European Library'))

    with allure.step("Picking DATA_PROVIDER."):
        browser.element('[data-qa="DATA_PROVIDER side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="National Library of the Netherlands DATA_PROVIDER field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('National Library of the Netherlands'))

    with allure.step("Picking COLOURPALETTE."):
        browser.element('[data-qa="COLOURPALETTE side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="#000000 COLOURPALETTE field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Black'))

    with allure.step("Picking IMAGE_ASPECTRATIO."):
        browser.element('[data-qa="IMAGE_ASPECTRATIO side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="landscape IMAGE_ASPECTRATIO field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Landscape'))

    with allure.step("Picking IMAGE_SIZE."):
        browser.element('[data-qa="IMAGE_SIZE side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="medium IMAGE_SIZE field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Medium 0.5-1MP (e.g. 850x850px)'))

    with allure.step("Picking MIME_TYPE."):
        browser.element('[data-qa="MIME_TYPE side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="image/jpeg MIME_TYPE field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('JPEG'))

    with allure.step("Picking RIGHTS."):
        browser.element('[data-qa="RIGHTS side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="*/publicdomain/mark/* RIGHTS field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Public Domain Mark'))

    with allure.step("Strange...."):
        browser.element('[data-qa="contentTier side facet dropdown button"]').should(be.clickable).click()
        browser.element('[data-qa="2 contentTier field"]').should(be.clickable).click()
        time.sleep(0.5)
        browser.element('[data-qa="side filters"]').should(have.text('Medium quality'))

    with allure.step("Testing RESET button."):
        browser.element('[data-qa="reset filters button"]').should(be.visible).click()
        browser.element('[data-qa="reset filters button"]').should(be.not_.visible)
"""