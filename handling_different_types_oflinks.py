from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#finding all the links in a web page.
# links=driver.find_elements(By.XPATH,'//a')
links=driver.find_elements(By.TAG_NAME,'a')
print("Total no of links: ", len(links))

for i in links:
    print(i.text)








