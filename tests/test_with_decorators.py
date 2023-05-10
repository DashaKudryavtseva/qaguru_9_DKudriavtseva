import allure
from selene import browser, by, be


def test_deorator_step_git():
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    click_issue()
    check_issue()


@allure.step('Открытие главной страницы')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Поиск репозитория')
def search_repository(name):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(name).press_enter()


@allure.step('Открытие репозитория')
def open_repository(name):
    browser.element(by.link_text(name)).click()


@allure.step('Клик по вкладке "Issues"')
def click_issue():
    browser.element('#issues-tab').click()


@allure.step('Проверка наличия #76')
def check_issue():
    browser.element(by.partial_text('#76')).should(be.visible)
