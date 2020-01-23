from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def guest_expect_basket_is_empty(self):
        basket_positions = self.browser.find_elements_by_css_selector('#basket_formset div')
        assert len(basket_positions) == 0, "basket is not empty"

    def guest_should_see_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty." in empty_basket_message, "Empty basket message is abcent"