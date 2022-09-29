from .base_page import BasePage
from .locators import CartContentLocators

class BasketPage(BasePage):
    def empty_cart_when_opened_from_main_page(self):
        assert self.is_not_element_present(*CartContentLocators.CART_CONT), 'The cart is not empty'

    def message_about_empty_cart_is_present(self):
        assert self.is_element_present(*CartContentLocators.MSG_EMPTY) and self.is_element_present(*CartContentLocators.LINK_CONTINUE_SHOPPING), 'There is no message to inform that the cart is empty'

