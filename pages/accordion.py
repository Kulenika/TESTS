from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.btn_elements = WebElement(driver, 'div:nth-child(4) > div > ul > #item-0 > span')
        self.text_element1 = WebElement(driver, '#section1Content>p')
        self.text_element2 = WebElement(driver, '#section1Heading')
        self.btn1_element = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.btn2_element = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.btn3_element = WebElement(driver, '#section3Content > p')



def visit(self):
    return self.driver.get(self.base_url)
