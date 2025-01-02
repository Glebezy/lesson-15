
from selene import browser, be


def test_github_desktop(browser_setup_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login').should(be.visible)


def test_github_mobile(browser_setup_mobile):
    browser.open('/')
    browser.element('//a[contains(text(), "Sign in")]').click()
    browser.element('#login').should(be.visible)
