import time

from pages.webtable_page import WebTables

def test_web_tables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.add_button.exist()
    web_tables.add_button.click()
    time.sleep(3)
    assert web_tables.modal_window.exist()
    web_tables.submit_button.click()
    assert web_tables.modal_window.exist()

    web_tables.first_name_mw.send_keys('Anna')
    web_tables.last_name_mw.send_keys('Kulevova')
    web_tables.e_mail_mw.send_keys('zizizi@mail.ru')
    web_tables.age_mw.send_keys('22')
    web_tables.salary_mw.send_keys('5000')
    web_tables.department_mw.send_keys('Legal')
    time.sleep(3)
    web_tables.submit_button.click()
    assert not web_tables.modal_window.exist()
    #как написать проверку, что новая запись добавлена в таблицу?
    web_tables.edit_4_button.click()
    assert web_tables.modal_window.exist()
    time.sleep(3)
    assert web_tables.first_name_mw.get_dom_attribute('value') == 'Anna'
    assert web_tables.last_name_mw.get_dom_attribute('value') == 'Kulevova'
    assert web_tables.e_mail_mw.get_dom_attribute('value') == 'zizizi@mail.ru'
    assert web_tables.age_mw.get_dom_attribute('value') == '22'
    assert web_tables.salary_mw.get_dom_attribute('value') == '5000'
    assert web_tables.department_mw.get_dom_attribute('value') == 'Legal'
    web_tables.first_name_mw.clear()
    web_tables.first_name_mw.send_keys('Sandra')
    web_tables.submit_button.click()
    time.sleep(3)
    # как написать проверку, что обновились данные в таблице?
    web_tables.delete4_btn.click()
    time.sleep(4)
    #как проверить, что записи больше нет?


def test_web_tables_2(browser):
    """"предусловия"""
    web_tables = WebTables(browser)
    web_tables.visit()
    time.sleep(2)
    web_tables.rows_button.scroll_to_element()
    web_tables.rows_button.click()
    web_tables.rows_button_5.click()
    time.sleep(2)

    ''''тест-кейс'''
    assert web_tables.previous_button.get_dom_attribute('disabled') == 'true'
    assert web_tables.next_button.get_dom_attribute('disabled') == 'true'


    web_tables.add_button.click()
    web_tables.first_name_mw.send_keys('Igor')
    web_tables.last_name_mw.send_keys('Igorev')
    web_tables.e_mail_mw.send_keys('zizi@mail.ru')
    web_tables.age_mw.send_keys('29')
    web_tables.salary_mw.send_keys('6000')
    web_tables.department_mw.send_keys('Legal')
    time.sleep(2)
    web_tables.submit_button.click()

    web_tables.add_button.click()
    web_tables.first_name_mw.send_keys('Ivan')
    web_tables.last_name_mw.send_keys('Ivanov')
    web_tables.e_mail_mw.send_keys('zi@mail.ru')
    web_tables.age_mw.send_keys('38')
    web_tables.salary_mw.send_keys('10000')
    web_tables.department_mw.send_keys('Legal')
    time.sleep(2)
    web_tables.submit_button.click()

    web_tables.add_button.click()
    web_tables.first_name_mw.send_keys('Olga')
    web_tables.last_name_mw.send_keys('Ivanova')
    web_tables.e_mail_mw.send_keys('ziz@mail.ru')
    web_tables.age_mw.send_keys('42')
    web_tables.salary_mw.send_keys('15000')
    web_tables.department_mw.send_keys('Legal')
    time.sleep(2)
    web_tables.submit_button.click()

    assert web_tables.next_button.exist()
    web_tables.next_button.click()
    time.sleep(3)
    assert web_tables.jump_to_page.get_dom_attribute('value') == '2'
    web_tables.previous_button.click()
    time.sleep(3)
    assert web_tables.jump_to_page.get_dom_attribute('value') == '1'







