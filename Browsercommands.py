import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(4)
# # driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
# driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# time.sleep(4)
# driver.close()


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(4)
# driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(8)
driver.quit()









