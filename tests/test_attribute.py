from pages.Text_Box import TextBox
def test_placeholder(browser):
    '''проверка значения атрибута элемента'''

    text_box = TextBox(browser)
    text_box.visit()
    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full Name'
