import time

from pages.demoqa import Demoqa
from pages.RadioButton import RadioButton
import pytest
@pytest.mark.skip   #пропустить тест
def test_decor(browser):
    demoqa = Demoqa(browser)
    demoqa.visit()
    assert demoqa.h5.check_count_elements(6)  #проверка, что заголовков h5 - 6 шт.

    for element in demoqa.h5.find_elements():
        assert element.text != ''  #проверка, что у заголовков есть текст


#@pytest.mark.skipif(True, reason='просто пропустить')

def test_radio_button(browser):
    radio_button = RadioButton(browser)
    if not radio_button.code_status():
        pytest.skip(reason=f'Страница {radio_button.base_url} недоступна')
    radio_button.visit()
    radio_button.yes.click_force()
    time.sleep(2)
    assert radio_button.text.get_text() == 'You have selected Yes'

    radio_button.impressive.click_force()
    time.sleep(2)
    assert radio_button.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio_button.no.get_dom_attribute('class')
    #assert radio_button.no.get_dom_attribute('class') == 'disabled'
