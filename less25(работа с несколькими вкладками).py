from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import unittest

class Teststr(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver= webdriver.Chrome()
        time.sleep(5)
        driver.get(link)
        input1 = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("1")
        input2 = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("2")
        input3 = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("3")
        button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()
        message1=driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Congratulations! You have successfully registered!", message1.text)
    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        time.sleep(5)
        driver.get(link)
        input1 = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("1")
        input2 = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("2")
        input3 = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("3")
        button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()
        message2=driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Congratulations! You have successfully registered!", message2.text)
if __name__ == "__main__":
    unittest.main()