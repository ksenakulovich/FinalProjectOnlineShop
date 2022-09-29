from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main > .price_color')
    CONFIRM_MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, '.alert:nth-child(1) > .alertinner > strong')
    CART_TOTAL = (By.CSS_SELECTOR, '.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')




