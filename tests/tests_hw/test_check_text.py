from selenium import webdriver
from selenium.webdriver.common.by import By


# ЗАДАЧА 1
driver = webdriver.Chrome()
driver.get('https://demoqa.com/')
# поиск элемента
icon1 = driver.find_element(By.CSS_SELECTOR, '#app > footer > span')
if icon1 is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

# ЗАДАЧА 2
driver = webdriver.Chrome()
driver.get('https://demoqa.com/')
def click_on_the_btn_elements(self):
    self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

