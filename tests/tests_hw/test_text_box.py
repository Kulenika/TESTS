import time

from pages.Text_Box import TextBox

'''Задание 1'''
def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.full_name.send_keys('Anna Nikonova')
    text_box.current_address.send_keys('Pushkina str. 16, Gorki')
    text_box.submit_btn.click_force()
    time.sleep(3)
    text_box.name.exist()
    text_box.address.exist()
    assert text_box.name.get_text() == 'Name:Anna Nikonova'
    assert text_box.address.get_text() == 'Current Address :Pushkina str. 16, Gorki'



