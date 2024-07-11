import os
import pathlib
import random

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

from steps.precondition_steps import PreconditionSteps


def pytest_addoption(parser):
    """ Parse pytest --option variables from shell """
    parser.addoption('--browser', help='Which test browser?',
                     default='chrome')
    parser.addoption('--local', help='local or CI?',
                     choices=['true', 'false'],
                     default='true')


@pytest.fixture(scope='session')
def test_browser(request):
    """ :returns Browser.NAME from --browser option """
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def local(request):
    """ :returns true or false from --local option """
    return request.config.getoption('--local')


@pytest.fixture(scope='function')
def remote_browser(test_browser, local, request) -> Remote:
    if local == 'false':
        if test_browser == 'firefox':
            driver = webdriver.Remote(
                options=webdriver.FirefoxOptions(),
                command_executor=f'http://selenium__standalone-{test_browser}:4444/wd/hub')
        elif test_browser == 'chrome':
            driver = webdriver.Remote(
                options=webdriver.ChromeOptions(),
                command_executor=f'http://selenium__standalone-{test_browser}:4444/wd/hub')
        else:
            raise ValueError(
                f'--browser="{test_browser}" is not chrome or firefox')
    else:
        download_dir = pathlib.Path(__file__).parent.resolve()
        options = Options()
        preferences = {"download.default_directory": os.path.join(download_dir, "download"),
                       "directory_upgrade": True,
                       "safebrowsing.enabled": True,
                       'intl.accept_languages': 'ru'}
        options.add_experimental_option("prefs", preferences)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def precondition():
    data = [{"name": f"Test"+str(random.randrange(1000, 9999)),
            "price": 1000},
            {"name": f"Test" + str(random.randrange(1000, 9999)),
             "price": 2000}
            ]
    data_1 = {
        "name": data[0]["name"],
        "section": "Платья",
        "description": "Модное платье из новой коллекции!",
        "color": "RED",
        "size": 40,
        "price": data[0]["price"],
        "params": "dress"}
    data_2 = {
        "name": data[1]["name"],
        "section": "Шорты",
        "description": "Новые шорты",
        "color": "Green",
        "size": 42,
        "price": data[1]["price"],
        "params": "shorts"}
    resp_1 = PreconditionSteps.create_item(data_1, "dress")
    try:
        assert resp_1['status'] == 'ok'
    except AssertionError:
        with allure.step("Первый товар не создан"):
            resp_1 = False
    resp_2 = PreconditionSteps.create_item(data_2, "shorts")
    try:
        assert resp_2['status'] == 'ok'
    except AssertionError:
        with allure.step("Второй товар не создан"):
            resp_2 = False
    yield data
    if resp_1 is not False:
        resp = PreconditionSteps.delete_item(resp_1['result']['id'])
        assert resp['status'] == 'ok'
    if resp_2 is not False:
        resp = PreconditionSteps.delete_item(resp_2['result']['id'])
        assert resp['status'] == 'ok'
