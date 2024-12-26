import pytest
from selenium import webdriver
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver.maximize_window()
    browser.config.type_by_js = True
    browser.config.driver_options = driver_options

    yield

    browser.quit()