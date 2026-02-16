from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

doubleclick=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(doubleclick).perform()
time.sleep(4)