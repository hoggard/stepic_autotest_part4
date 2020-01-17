from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time
import pytest


#@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#def test_guest_can_add_product_to_basket(browser, promo_offer):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()                      # открываем страницу товара
#    page.add_to_basket()          # выполняем метод страницы - добавляем товар в корзину
#    page.solve_quiz_and_get_code()   # получаем код для скидки
#    page.should_be_message_about_adding()  # проверяем сообщение о добавлении в корзину и название товара
#    page.should_be_message_basket_total()   # проверяем цену за товар и стоимость корзины

@pytest.mark.xfail (reason="bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.add_to_basket()  # выполняем метод страницы - добавляем товар в корзину
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе

@pytest.mark.xfail (reason="bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.add_to_basket()  # выполняем метод страницы - добавляем товар в корзину
    time.sleep(2)
    page.should_disappeared_success_message() # Проверяем, что нет сообщения об успехе

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = BasePage(browser, browser.current_url)
    login_page.should_be_login_link()