from .base_page import BasePage
from .locators import LoginPageLocators, LogInLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.current_url
        assert 'login' in login_link, 'The link does not contain the "login" substring'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LogInLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LogInLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        conf_password_field = self.browser.find_element(*LogInLocators.CONF_PASSWORD_FIELD)
        conf_password_field.send_keys(password)
        button = self.browser.find_element(*LogInLocators.REG_BUTTON)
        button.click()



