from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
mouse = driver.find_element(By.XPATH,"//button[normalize-space()='Point Me']")

act= ActionChains(driver)
act.move_to_element(mouse).click().perform()
time.sleep(4)