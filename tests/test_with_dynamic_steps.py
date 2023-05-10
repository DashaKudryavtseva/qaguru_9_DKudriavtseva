import allure
from selene import browser, by, be


def test_git_dynamic_step():
    with allure.step('Открытие главной страницы'):
        browser.open('https://github.com/')

    with allure.step('Поиск репозитория'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys(
            'eroshenkoam/allure-example'
        ).press_enter()

    with allure.step('Открытие репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Клик по вкладке "Issues"'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия #76'):
        browser.element(by.partial_text('#77')).should(be.visible)
