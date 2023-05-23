from pages.base_page import BasePage
from components.components import WebElement


class SaucedemoPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)
        self.username = WebElement(driver, '#user-name')
        self.password = WebElement(driver, '#password')
        self.login = WebElement(driver, '#login-button')




