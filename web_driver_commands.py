from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#application commands
driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source) # you want to do some validation on the entire page code.


#conditional_ statemments

# search = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print("Display status: ",search.is_enabled())
# print("Display status: ",search.is_displayed())
# print("Display status: ",search.is_selected())


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# male = driver.find_element(By.CSS_SELECTOR,"#gender-male")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
# female = driver.find_element(By.XPATH,"//input[@id='gender-female']")
# print(male.is_selected())
# print(female.is_selected())









