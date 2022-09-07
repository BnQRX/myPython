from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    time.sleep(10)
    browser.get(link)

    input1 = browser.find_element(By.NAME, first_name)
    input1.send_keys("1")
    input2 = browser.find_element(By.NAME, last_name)
    input2.send_keys("2")
    input3 = browser.find_element(By.CLASS_NAME, form-control.sity)
    input3.send_keys("3")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("4")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()