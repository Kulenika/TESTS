from pages.base_page import BasePage
from components.components import WebElement

class InventoryPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/inventory.html'
        super().__init__(driver, self.base_url)
        self.labs_backpack_add = WebElement(driver, '#add-to-cart-sauce-labs-backpack')
        self.bike_light_add = WebElement(driver, '#add-to-cart-sauce-labs-bike-light')
        self.shopping_cart_btn = WebElement(driver, '#shopping_cart_container > a')
        self.menu_btn = WebElement(driver, '#react-burger-menu-btn')
        self.logout_btn = WebElement(driver, '#logout_sidebar_link')






