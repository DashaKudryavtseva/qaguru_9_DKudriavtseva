from selene import browser, by, be


def test_git_selene():
    browser.open('https://github.com/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(
        'eroshenkoam/allure-example'
    ).press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#77')).should(be.visible)
