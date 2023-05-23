from pages.alerts import AlertsPage

import time

def test_check_alert(browser):
    alert_page = AlertsPage(browser)
    alert_page.visit()
    alert_page.timer_button.click()
    time.sleep(5)
    assert alert_page.alert()
    alert_page.alert().accept()
