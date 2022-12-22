from blaze.src.pages.locators.CartPageLocator import CartPageLocator
from blaze.src.SeleniumExtended import SeleniumExtended


class CartPage(CartPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
