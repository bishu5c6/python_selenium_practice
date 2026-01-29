from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
#tagid
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("bishu")
#tag_class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("biswanth@gmail.com")

#attribute along with the value
# driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username webauthn"]').send_keys("123erf")

#tage class and attribute
driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid="royal-email"]').send_keys("bishu@gmail.conm")
time.sleep(4)



