import time

from pages.webtable_page import WebTables

def test_webtables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.last_name_click.click()
    time.sleep(2)
    #assert 'rt-th rt-resizable-header -sort-asc -cursor-pointer' in web_tables.last_name_click.get_text('class')
    web_tables.first_name_click.click()
    time.sleep(2)
    web_tables.age_click.click()
    time.sleep(2)
    web_tables.email_click.click()
    time.sleep(2)
    web_tables.salary_click.click()
    time.sleep(2)
    web_tables.department_click.click()
    time.sleep(2)

    #assert web_tables.first_name_sort.get_dom_attribute('class') ==
