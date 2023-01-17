from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.example.com")

text_box = driver.find_element_by_xpath("//input[@name='example']")

text_box.send_keys("example text")

button = driver.find_element_by_xpath("//button[@name='submit']")
button.click()

driver.quit()
