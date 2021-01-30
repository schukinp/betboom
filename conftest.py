import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene.api import config, browser
from webdriver_manager.chrome import ChromeDriverManager


chromedriver_path = ChromeDriverManager().install()


@pytest.fixture()
def set_browser():
    """Настроить браузер"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    driver.maximize_window()
    config.timeout = 10
    browser.set_driver(driver)
