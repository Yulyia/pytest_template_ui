import re

import allure
from selenium.webdriver import Keys

from locators.base_page_locators import BasePageLocators


class MainPageSteps:

    @staticmethod
    @allure.step("Проверка на наличие информационного сообщения")
    def alert_is_visible(page):
        alert = page.find_element(BasePageLocators.alert)
        text = alert.text
        color = alert.value_of_css_property("color")
        assert "Это ТЕСТОВЫЙ магазин!" in text
        assert color == 'rgba(114, 28, 36, 1)'

    @staticmethod
    @allure.step("Добавление продукта в корзину")
    def add_product_to_shopping_cart(page, locator, quantity=1):
        product = page.find_to_be_clickable(locator)
        product.click()
        price_string = page.find_element(BasePageLocators.price_product).text
        price = int(re.search('\d+', price_string)[0])
        sum_price = price * quantity
        input_quantity = page.find_element(BasePageLocators.input_quantity)
        input_quantity.send_keys(quantity)
        button = page.find_to_be_clickable(BasePageLocators.add)
        button.click()
        return sum_price

    @staticmethod
    @allure.step("Поиск товара по наименованию")
    def search_product_by_name(page, name):
        search = page.find_element(BasePageLocators.search_input)
        search.send_keys(name)
        search.send_keys(Keys.ENTER)
