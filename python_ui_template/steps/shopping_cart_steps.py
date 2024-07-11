import allure

from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class ShoppingCartSteps(BasePage):

    @staticmethod
    @allure.step("Проверка отображения товаров в корзине")
    def assertion_product_in_shopping_cart(page, quantity, price):
        with allure.step("Проверка отображения кол-ва товаров на главной странице (иконка) в корзине"):
            shopping_cart = page.find_to_be_clickable(BasePageLocators.shopping_cart)
            assert int(shopping_cart.text) == quantity
        with allure.step("Проверка общей суммы всех товаров в корзине"):
            shopping_cart.click()
            total = page.find_element(BasePageLocators.total_sum).text
            assert int(total) == price

    @staticmethod
    @allure.step("Проверка общей суммы в корзине в соответствии со сгенерированными данными")
    def assertion_summ(page, data, quantity_1, quantity_2):
        total = page.find_element(BasePageLocators.total_sum).text
        sum = data[0]['price']*quantity_1 + data[1]['price']*quantity_2
        assert int(total) == sum

    @staticmethod
    @allure.step("Возврат на главную страницу для выбора следующего товара")
    def return_to_main_page(page):
        all_products = page.find_element(BasePageLocators.all_products)
        all_products.click()



