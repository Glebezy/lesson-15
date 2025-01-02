import pytest
from selene import browser, be


@pytest.fixture
def custom_browser_size(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width + 100
    browser.config.window_height = height - 100


@pytest.mark.parametrize("custom_browser_size", [(1920, 1080), (1280, 720)], ids=['1920_1080', '1280_720'], indirect=True)
def test_github_desktop(custom_browser_size):
    browser.open('/')
    browser.element('.HeaderMenu .HeaderMenu-link--sign-in').click()
    browser.element('#login form').should(be.visible)


@pytest.mark.parametrize("custom_browser_size", [(360, 740), (375, 667)], ids=['360_740', '375_667'], indirect=True)
def test_github_mobile(custom_browser_size):
    browser.open('/')
    browser.element('a[aria-label=Homepage]+div a').click()
    browser.element('#login form').should(be.visible)
