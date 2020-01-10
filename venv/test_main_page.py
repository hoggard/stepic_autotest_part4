from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


#1
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

#2
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#3
#def test_guest_should_go_correct_login_url(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page1 = MainPage(browser, link)
#    page1.open()
#    page1.go_to_login_page()
#    page2 = LoginPage(browser, link)
#    page2.should_be_login_url()

#4
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
