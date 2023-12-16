from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    print(x)
    x_element1 = browser.find_element(By.ID, "num2")
    x1 = x_element1.text
    print(x1)
    y = int(x)+int(x1)
    print(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла