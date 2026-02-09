from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.find_element(By.XPATH,"//input[@id='sunday']").click()
# time.sleep(4)

#you want to click on all checkboxes you need to use for loop.
checkboxws=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day') ]")
print(len(checkboxws))
# for i in checkboxws:
#     i.click()
#
# time.sleep(4)

#approach 2
# for i in range(len(checkboxws)):
#     checkboxws[i].click()
# time.sleep(4)

#based on condition
#select check multiple checkboxes by choice
# for i in checkboxws:
#     weekname = i.get_attribute('id')
#     if weekname =='monday' or weekname=='sunday':
#         i.click()

#select last 2 checkboxes:

# for i in range(len(checkboxws)-2, len(checkboxws)):
#     checkboxws[i].click()
# time.sleep(3)

#select first 2 checkboxes:
# for i in range(len(checkboxws)):
#     if i<2:
#         checkboxws[i].click()
# time.sleep(3)

#clearing all the checkboxes:
for i in checkboxws:
    if i.is_selected():
        i.click()

