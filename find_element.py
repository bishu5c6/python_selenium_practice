from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

#matching with the single element

# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("bishu")
# time.sleep(5)

#2) locator matching with multiple web elements
# e=driver.find_element(By.XPATH,"//nav[@class='footer-navigation']//a")
# print(e.text)

#3) Element not available it throws no element such exception.
login=driver.find_element(By.XPATH,"//a[normalize-space()='Log in']")
login.click()
time.sleep(4)