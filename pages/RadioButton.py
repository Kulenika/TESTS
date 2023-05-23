from pages.base_page import BasePage
from components.components import WebElement
class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)
        self.yes = WebElement(driver, 'div:nth-child(2) > label')
        self.no = WebElement(driver, 'div.custom-control.disabled.custom-radio.custom-control-inline > label')
        self.impressive = WebElement(driver, '#impressiveRadio')
        self.text = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p')




