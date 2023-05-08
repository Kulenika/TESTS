from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.text_element1.visible()
    accordion_page.text_element2.click()
    time.sleep(2)
    assert not accordion_page.text_element1.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.btn1_element.visible()
    assert accordion_page.btn2_element.visible()
    assert accordion_page.btn3_element.visible()
    time.sleep(2)
    assert not accordion_page.btn1_element.visible()
    assert not accordion_page.btn2_element.visible()
    assert not accordion_page.btn3_element.visible()
