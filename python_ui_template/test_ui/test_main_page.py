import logging

import allure


from python_ui_template.constans import HOST
from python_ui_template.pages.base_page import BasePage
from python_ui_template.steps.main_page_steps import MainPageSteps
from python_ui_template.steps.shopping_cart_steps import ShoppingCartSteps


def test_1(remote_browser):
    remote_browser.get('https://google.com')


@allure.title("Проверка отображения информационного сообщения на главной странице")
def test_assertion_visible_alert(remote_browser):
    with allure.step("Открытие страницы"):
        page = BasePage(remote_browser, HOST)
        page.open()
    MainPageSteps.alert_is_visible(page)


@allure.title("Проверка добавления произвольного товара в корзину")
def test_add_one_random_product_to_shopping_cart(remote_browser):
    with allure.step("Открытие страницы"):
        page = BasePage(remote_browser, HOST)
        page.open()

    logging.info("Добавление жёлтого платья в корзину")
    sum_price_1_product = MainPageSteps.add_product_to_shopping_cart(page, BasePageLocators.dress, quantity=1)

    ShoppingCartSteps.assertion_product_in_shopping_cart(page, quantity=1, price=sum_price_1_product)
    ShoppingCartSteps.return_to_main_page(page)


@allure.title("Проверка добавления нескольких товаров в корзину, которые были сгенерированы заранее")
def test_add_some_product_to_shopping_cart(remote_browser, precondition):
    quantity_1 = 2
    quantity_2 = 1
    with allure.step("Открытие страницы"):
        page = BasePage(remote_browser, HOST)
        page.open()
    MainPageSteps.search_product_by_name(page, precondition[0]["name"])
    logging.info(f"Добавление {precondition[0]['name']} в корзину")
    sum_price_1_product = MainPageSteps.add_product_to_shopping_cart(page, BasePageLocators.product, quantity=quantity_1)

    ShoppingCartSteps.assertion_product_in_shopping_cart(page, quantity_1, sum_price_1_product)
    ShoppingCartSteps.return_to_main_page(page)

    logging.info(f"Добавление второго {precondition[1]['name']} продукта в корзину")
    MainPageSteps.search_product_by_name(page, precondition[1]["name"])
    sum_price_2_product = MainPageSteps.add_product_to_shopping_cart(page, BasePageLocators.product,
                                                                     quantity=quantity_2)

    ShoppingCartSteps.assertion_product_in_shopping_cart(page, quantity_1+quantity_2,
                                                         sum_price_1_product+sum_price_2_product)
    ShoppingCartSteps.assertion_summ(page, precondition, quantity_1, quantity_2)




