import datetime
from datetime import datetime

import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser: webdriver.Remote, url: str):
        self.browser = browser
        self.url = url

    with allure.step("Открытие страницы"):
        def open(self):
            self.browser.get(self.url)

    with allure.step("Поиск элемента с неявным ожиданием на отображение"):
        def find_element(self, locator, time=10):
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                           message=f"Can't find element by locator {locator}")
    with allure.step("Поиск элемента с неявным ожиданием на кликабельность"):
        def find_to_be_clickable(self, locator, time=10):
            return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                           message=f"Can't find element by locator {locator}")

    with allure.step("Получение скриншота"):
        def take_screenshot(self):
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            name_file = f"screenshot-{now}.png"
            self.browser.get_screenshot_as_file(name_file)
            print(f"Taked screenshot: {name_file}")


