from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

#1
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()          # выполняем метод страницы - добавляем товар в корзину
    page.solve_quiz_and_get_code()   # выводим код для скидки
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()