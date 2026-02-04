from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")


# element=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(element))
# print(element[0].send_keys("bsihsu"))
# time.sleep(5)

#2) locator matching with multiple web elements
# e=driver.find_elements(By.XPATH,"//nav[@class='footer-navigation']//a")
# print(len(e))
# # print(e[13].text)
# for i in e:
#     print(i.text)
#3) Element not available it throws no element such exception.
login=driver.find_elements(By.XPATH,"//a[normalize-space='Log in']")
login.click()
# time.sleep(4)