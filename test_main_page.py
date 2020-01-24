from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# тесты запускаем так: pytest -v --tb=line --language=en -m test_main_page.py

#1 Тестируем возможность перейти на страницу логина (step 4.2.4, 4.2.9)
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

#2 Тестируем наличие ссылки логина (step 4.2.5)
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()          # проверяем наличие ссылки на логин

#3 Тестируем переход в корзину с гравной страницы и пустоту корзины (step 4.3.10)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened_from_another_page()
    page.guest_expect_basket_is_empty()
    page.guest_should_see_empty_basket_message()
