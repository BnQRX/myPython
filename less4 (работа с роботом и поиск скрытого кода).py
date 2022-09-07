from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "https://suninjuly.github.io/math.html"

try:
    driver= webdriver.Chrome()
    time.sleep(10)
    driver.get(link)
    option1 = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = driver.find_element(By.ID, "robotsRule")
    option2.click()
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    endelem = driver.find_element(By.ID, "answer")
    endelem.send_keys(y)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    driver.quit()