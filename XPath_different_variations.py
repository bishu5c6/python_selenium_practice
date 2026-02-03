import time

from selenium  import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.maximize_window()

#absolutive xpath
# driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input[1]").send_keys('Biswanth')
# time.sleep(4)

#relative xpath
driver.find_element(By.XPATH,"//input[@id='name']").send_keys('bisesnth')

time.sleep(4)



