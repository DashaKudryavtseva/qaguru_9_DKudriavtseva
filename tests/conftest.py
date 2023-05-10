import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_configuration():
    browser.config.browser_name = "chrome"
    browser.config.window_height = 1920
    browser.config.window_width = 1080
