from components.components import WebElement
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/cart.html'
        super().__init__(driver, self.base_url)
        self.link_1 = WebElement(driver, '#item_4_title_link > div')
        self.link_2 = WebElement(driver, '#item_0_title_link > div')
        self.delete_1 = WebElement(driver, '#remove-sauce-labs-backpack')
        self.delete_2 = WebElement(driver, '#remove-sauce-labs-bike-light')
        self.empty_cart = WebElement(driver, '#cart_contents_container > div > div.cart_list')
        self.link_3 = WebElement(driver, '#item_4_title_link > div')
        self.link_4 = WebElement(driver, '#item_0_title_link > div')






