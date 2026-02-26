from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import os
location=os.getcwd()

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://qa-automation-practice.netlify.app/file-upload.html")
driver.maximize_window()
upload=driver.find_element(By.XPATH,"//input[@id='file_upload']")
act=ActionChains(driver)
act.click(upload).perform()
act.send_keys(("C:/Users/temp/Downloads/Z100103.pdf"))
time.sleep(4)

