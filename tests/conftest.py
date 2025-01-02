import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720)], ids=['1920_1080', '1280_720'])
def browser_setup_desktop(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(360, 740), (375, 667)], ids=['360_740', '375_667'])
def browser_setup_mobile(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 720), (360, 740), (375, 667)],
                ids=['1920_1080', '1280_720', '360_740', '375_667'])
def browser_setup(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    if width >= 720:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()
