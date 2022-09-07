from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/get_attribute.html"

try:
    driver= webdriver.Chrome()
    time.sleep(10)
    driver.get(link)
    option1 = driver.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = driver.find_element(By.ID, "robotsRule")
    option2.click()

    x_element = driver.find_element(By.ID, "treasure")
    x=x_element.get_attribute("valuex")
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