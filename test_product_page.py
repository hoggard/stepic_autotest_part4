from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest

# тесты запускаем так: pytest -v --tb=line --language=en -m need_review test_product_page.py

#1 Тестируем добавление товара в корзину и проверку стоимости корзины (step 4.3.2, 4.3.4)
@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу товара
    page.add_to_basket()          # выполняем метод страницы - добавляем товар в корзину
    page.solve_quiz_and_get_code()   # получаем код для скидки
    page.should_be_message_about_adding()  # проверяем сообщение о добавлении в корзину и название товара
    page.should_be_message_basket_total()   # проверяем цену за товар и стоимость корзины

#2 Забагованный тест, проверяющий сообщение о добавлении товара в корзину (step 4.3.6)
@pytest.mark.xfail (reason="bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.add_to_basket()  # выполняем метод страницы - добавляем товар в корзину
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе

#3 Тестируем, что на странице товара нет сообщения об успешном добавлении (step 4.3.6)
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе

#4 Забагованный тест, проверяющий, что нет сообщений об успешном добавлении товара (step 4.3.6)
@pytest.mark.xfail (reason="bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу товара
    page.add_to_basket()  # выполняем метод страницы - добавляем товар в корзину
    time.sleep(2)
    page.should_disappeared_success_message() # Проверяем, что нет сообщения об успехе

#5 Тестируем наличие на странице продукта ссылки на страницу регистрации (step 4.3.8)
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#6 Тестируем возможность перехода со страницы товара на страницу регистрации (step 4.3.8)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = BasePage(browser, browser.current_url)
    login_page.should_be_login_link()

#7 Тестируем переход со страницы товара в корзину  (step 4.3.10)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened_from_another_page()
    page.guest_expect_basket_is_empty()
    page.guest_should_see_empty_basket_message()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    # Тестируем авторизацию нового пользователя (Setup)  (step 4.3.11)
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(password = "abracadabra123", email = str(time.time()) + "@fakemail.org")
        self.page.should_be_authorized_user()

    #8 Тестируем, что на странице товара нет сообщения об успешном добавлении после регистрации  (step 4.3.11)
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу товара
        page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе

    #9 Тестируем добавление товара в корзину и проверку стоимости корзины после регистрации  (step 4.3.11)
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу товара
        page.add_to_basket()  # выполняем метод страницы - добавляем товар в корзину
        page.solve_quiz_and_get_code()  # получаем код для скидки
        page.should_be_message_about_adding()  # проверяем сообщение о добавлении в корзину и название товара
        page.should_be_message_basket_total()  # проверяем цену за товар и стоимость корзины