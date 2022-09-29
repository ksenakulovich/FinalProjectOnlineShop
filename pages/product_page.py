from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
from .base_page import BasePage
import math


class ProductPage(BasePage):
    def add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON_PROD)
        cart_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        return item_price

    def get_conf_message_about_item_name(self):
        confirmation_msg_part = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE_ITEM_NAME).text
        return confirmation_msg_part

    def get_cart_total(self):
        cart_total = self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
        return cart_total

    def product_name_should_be_in_conf_msg(self, prod_name, msg_part):
        assert prod_name == msg_part, 'The item name on the product page differs from the one added to the cart'

    def cart_total_should_equal_to_price(self, item_pr, cart_tot):
        assert item_pr == cart_tot, 'The item price differs from the cart total'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def element_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The element is still present, but should be disappeared"

