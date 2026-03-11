from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
loc=os.getcwd()
driver = webdriver.Chrome()



driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.save_screenshot("C:/Users/temp/Downloads/selenium_webdriver/1.png")
driver.save_screenshot(os.getcwd()+"/1.png")
driver.get_screenshot_as_file(os.getcwd()+"/1.png")