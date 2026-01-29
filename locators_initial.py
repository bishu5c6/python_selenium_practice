from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"#small-searchterms").send_keys("Play-Station-5")
# # driver.find_element(By.LINK_TEXT,"Search").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"searc").click()

a=driver.find_elements(By.TAG_NAME,"a")
print(len(a))

time.sleep(4)


