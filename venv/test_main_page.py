from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
import pytest

#1 Тестируем возможность перейти на страницу логина
def test_guest_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

#2 Тестируем наличие ссылки логина
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#3 Тестируем правильность URL страницы логина
def test_guest_should_go_correct_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page1 = MainPage(browser, link)
    page1.open()
    page1.go_to_login_page()
    page2 = LoginPage(browser, link)
    page2.should_be_login_url()

#4 Тестируем видимость полей входа и регистрации
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

#5 Тестируем возможность перехода на страницу логина с гласной страницы
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

#6 Тестируем переход в корзину с гравной страницы и пустоту корзины
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened_from_another_page()
    page.guest_expect_basket_is_empty()
    page.guest_should_see_empty_basket_message()
    
