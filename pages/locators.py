from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main > .price_color')
    CONFIRM_MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, '.alert:nth-child(1) > .alertinner > strong')
    CART_TOTAL = (By.CSS_SELECTOR, '.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')
    CART_BUTTON_PROD = (By.CSS_SELECTOR, '.btn-add-to-basket')


class CartContentLocators:
    CART_CONT = (By.CSS_SELECTOR, '.basket_summary')
    MSG_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
    LINK_CONTINUE_SHOPPING = (By.XPATH, '//*[@id="content_inner"]/p/a')


class LogInLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '#register_form input[name="registration-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    CONF_PASSWORD_FIELD = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]')
    REG_BUTTON = (By.CSS_SELECTOR, "button[name = 'registration_submit']")
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success >  .alertinner')






