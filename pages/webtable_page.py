from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.delete_button = WebElement(driver, 'span[title=“Delete”]')
        self.add_button = WebElement(driver, '#addNewRecordButton')
        self.modal_window = WebElement(driver, 'div.fade.modal.show > div > div')
        self.first_name_mw = WebElement(driver, '#firstName')
        self.last_name_mw = WebElement(driver, '#lastName')
        self.e_mail_mw = WebElement(driver, '#userEmail')
        self.age_mw = WebElement(driver, '#age')
        self.salary_mw = WebElement(driver, '#salary')
        self.department_mw = WebElement(driver, '#department')
        self.submit_button = WebElement(driver, '#submit')
        self.edit_4_button = WebElement(driver, '#edit-record-4 > svg > path')
        self.delete4_btn = WebElement(driver, '#delete-record-4 > svg > path')
        self.rows_button = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.rows_button_5 = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.previous_button = WebElement(driver, 'div > div.-previous > button')
        self.next_button = WebElement(driver, 'div > div.-next > button')
        self.jump_to_page = WebElement(driver, 'span.-pageInfo > div > input[type=number]')








