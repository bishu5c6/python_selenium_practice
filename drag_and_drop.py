import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()

img1 = driver.find_element(By.XPATH,"//div[@class='col-xs-10 col-xs-offset-2']//img[@id='angular']")
img1_src = driver.find_element(By.XPATH,"//div[@id='droparea']")

act = ActionChains(driver)
act.drag_and_drop(img1,img1_src).perform()
time.sleep(5)




