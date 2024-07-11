from selenium.webdriver.common.by import By


class BasePageLocators:
    alert = (By.CSS_SELECTOR, "div.alert-danger")
    product = (By.CSS_SELECTOR, "a>p")
    input_quantity = (By.ID, "exampleCount")
    add = (By.CSS_SELECTOR, "button.btn-primary")
    shopping_cart = (By.CSS_SELECTOR, "div.float-right")
    dress = (By.XPATH, "//*[.='Платье желтое']")
    all_products = (By.CSS_SELECTOR, "li.breadcrumb-item>a")
    price_product = (By.CSS_SELECTOR, "span.label-primary")
    total_sum = (By.XPATH, "//*[.='Итого']/following-sibling::td")
    search_input = (By.CSS_SELECTOR, "input.mr-sm-2")


