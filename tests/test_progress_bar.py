import time
from pages.ProgressBar import ProgressBar

def test_progress_bar(browser):
    progress_bar = ProgressBar(browser)
    progress_bar.visit()
    time.sleep(2)
    progress_bar.start_stop_btn.click()

    while True:
        if progress_bar.progress_bar_value.get_dom_attribute('aria-valuenow') == '51':
            progress_bar.start_stop_btn.click()
            break

    time.sleep(2)

'''ИЛИ:'''

    #while not progress_bar.progress_bar_value.get_dom_attribute('aria-valuenow') == '51':
        #progress_bar.start_stop_btn.click()

    #assert progress_bar.progress_bar_value.get_dom_attribute('aria-valuenow') == '51'