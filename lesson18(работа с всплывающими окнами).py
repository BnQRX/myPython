from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/alert_accept.html"

try:
    driver= webdriver.Chrome()
    time.sleep(10)
    driver.get(link)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert=driver.switch_to.alert
    alert.accept()
    x= driver.find_element(By.ID, "input_value")
    x = x.text
    ended = calc(x)
    kek= driver.find_element(By.ID, "answer")
    kek.send_keys(ended)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    driver.quit()