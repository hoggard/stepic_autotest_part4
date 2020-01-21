from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/' , "login-link has wrong url"
        
    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_ADRESS), "Login Email-adress is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login Password is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_ADRESS), "Register Email-adress is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register Password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Confirm Register Password is not presented"

    def register_new_user(email, password):
        email = str(time.time()) + "@fakemail.org"
        #password = "abracadabra123"
        self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_ADRESS).send_keys(email)
        self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.is_element_present(*LoginPageLocators.REGISTER_BUTTON).click()


