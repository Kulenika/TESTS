from pages.base_page import BasePage
from components.components import WebElement
class Herokuapp2(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)
        self.add_element = WebElement(driver, '#content > div > button')
        self.delete_btn = WebElement(driver, '#elements > button:nth-child(1)')
        self.delete_btn1 = WebElement(driver, '//*[@id="elements"]/button[1]')
        self.delete_btn2 = WebElement(driver, '//*[@id="elements"]/button[2]')
        self.delete_btn3 = WebElement(driver, '//*[@id="elements"]/button[3]')
        self.delete_btn4 = WebElement(driver, '//*[@id="elements"]/button[4]')


