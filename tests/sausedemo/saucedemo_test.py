from pages.saucedemo.saucedemo_main import SaucedemoPage
from pages.saucedemo.saucedemo_product import InventoryPage
from pages.saucedemo.saucedemo_cart import CartPage
import time
def test_saucedemo(browser):
    saucedemo = SaucedemoPage(browser)
    inventory = InventoryPage(browser)
    saucedemo.visit()
    saucedemo.username.send_keys('standard_user')
    saucedemo.password.send_keys('secret_sauce')
    saucedemo.login.click()
    assert inventory.equal_url()


''''Задача 2'''
def test_task_2(browser):
    saucedemo = SaucedemoPage(browser)
    inventory = InventoryPage(browser)
    cart = CartPage(browser)
    saucedemo.visit()
    saucedemo.username.send_keys('standard_user')
    saucedemo.password.send_keys('secret_sauce')
    saucedemo.login.click()
    inventory.labs_backpack_add.click()
    inventory.bike_light_add.click()
    time.sleep(3)
    inventory.shopping_cart_btn.click()
    time.sleep(2)
    assert cart.link_1.get_text() == 'Sauce Labs Backpack'
    assert cart.link_2.get_text() == 'Sauce Labs Bike Light'
    time.sleep(2)
    cart.delete_1.click()
    cart.delete_2.click()
    #как проверить, что корзина пустая?


''''Задача 3'''

def test_task_3(browser):
    saucedemo = SaucedemoPage(browser)
    inventory = InventoryPage(browser)
    cart = CartPage(browser)
    saucedemo.visit()
    saucedemo.username.send_keys('standard_user')
    saucedemo.password.send_keys('secret_sauce')
    saucedemo.login.click()
    inventory.labs_backpack_add.click()
    inventory.bike_light_add.click()
    time.sleep(3)
    inventory.menu_btn.click()
    time.sleep(3)
    inventory.logout_btn.click()
    time.sleep(2)
    saucedemo.username.send_keys('standard_user')
    saucedemo.password.send_keys('secret_sauce')
    saucedemo.login.click()
    inventory.shopping_cart_btn.click()
    assert cart.link_4.get_text() == 'Sauce Labs Bike Light'
    assert cart.link_3.get_text() == 'Sauce Labs Backpack'



