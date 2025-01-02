from selene import browser, be
import pytest


def test_github_desktop(browser_setup):
    if browser_setup == 'mobile':
        pytest.skip(reason='Разрешение экрана не соответствует')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


def test_github_mobile(browser_setup):
    if browser_setup == 'desktop':
        pytest.skip(reason='Разрешение экрана не соответствует')
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
