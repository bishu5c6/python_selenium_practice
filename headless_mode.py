from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def headless_chrome():

    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(options=ops)
    return driver


driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)