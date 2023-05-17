import time

from pages.webtable_page import WebTables

def test_webtables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    assert not web_tables.no_rows_found.exist()

    while web_tables.delete_button.exist():
        web_tables.delete_button.click()

    time.sleep(5)
    assert web_tables.no_rows_found.exist()


