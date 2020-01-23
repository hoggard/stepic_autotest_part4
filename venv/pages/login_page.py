from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/' 
        assert self.browser.current_url == login_link , "login-link has wrong url"
        
    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_ADRESS), "Login Email-adress is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login Password is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_ADRESS), "Register Email-adress is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register Password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Confirm Register Password is not presented"

    def register_new_user(self, email, password):
        # регистрируем нового пользователя
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


