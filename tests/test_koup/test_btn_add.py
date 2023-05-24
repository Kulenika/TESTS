from pages.herokuapp import Herokuapp
from pages.herokuapp2 import Herokuapp2
import time

def test_add_remove(browser):
    HeroKuapp = Herokuapp(browser)
    HeroKuapp.visit()
    assert HeroKuapp.equal_url()
    assert HeroKuapp.add_remove_btn.get_text() == 'Add/Remove Elements'
    HeroKuapp.add_remove_btn.click()
    HeroKuapp2 = Herokuapp2(browser)
    assert HeroKuapp2.add_element.get_dom_attribute('onclick') == 'addElement()'
    HeroKuapp2.equal_url()
    for i in range(4):
        HeroKuapp2.add_element.click()
        time.sleep(3)
    #assert HeroKuapp2.delete_btn.check_count_elements(count=4)

    #проверка для всех элементов
    for element in HeroKuapp2.delete_btn.find_elements():
        assert element.text == 'Delete'

   #When Кликнуть на каждую кнопку "Delete"
    while HeroKuapp2.delete_btn.exist():
        HeroKuapp2.delete_btn.click()
        time.sleep(3)


    assert not HeroKuapp2.delete_btn.exist()





