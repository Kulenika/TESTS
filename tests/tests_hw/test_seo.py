from pages.demoqa import Demoqa
from pages.accordion import Accordion
from pages.alerts import AlertsPage
from pages.browser_tab import BrowserTab

import time
import pytest

def test_check_title(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    assert browser.title == demo_qa_page.pageData['title']

@pytest.mark.parametrize('pages', [Accordion, AlertsPage, Demoqa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
   
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'



