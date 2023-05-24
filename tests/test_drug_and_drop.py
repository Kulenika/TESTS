from pages.droppable import DroppablePage
import time
from selenium.webdriver import ActionChains

def test_drug_and_drop(browser):
    droppable = DroppablePage(browser)
    action_chains = ActionChains(browser)
    droppable.visit()

    assert droppable.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')

    action_chains.drag_and_drop(
        droppable.drag.find_element(),   # element
        droppable.drop.find_element()   #target
    ).perform()
    time.sleep(1)

    assert droppable.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop_by_offset(
        droppable.drop.find_element(),   #element
        - 200, 0  #target
    ).perform()
    time.sleep(1)
    assert droppable.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')



