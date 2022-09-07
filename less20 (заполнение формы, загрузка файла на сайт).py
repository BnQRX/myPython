from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time 

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get(link)
    input1 = driver.find_element(By.NAME, "firstname").send_keys("1")
    input2 = driver.find_element(By.NAME, "lastname").send_keys("2")
    input3 = driver.find_element(By.NAME, "email").send_keys("3")
    input4 = driver.find_element(By.ID, "file").send_keys("E:\puk.txt")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.submit()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()