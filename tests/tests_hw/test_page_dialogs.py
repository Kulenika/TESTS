from pages.modal_dialogs import ModalDialogs
import time


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.buttons_modal.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()

    modal_dialogs.icon_md.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(3)
    browser.forward()
    assert modal_dialogs.equal_url()
    assert browser.title == modal_dialogs.pageData['title']
    browser.set_window_size(1000, 1000)
 

