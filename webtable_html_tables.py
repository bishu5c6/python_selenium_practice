from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.maximize_window()

#1) count no of rows and cloumns
#2) read specific row and data.
#3) read all rows and data
#4) read data based on conitions.

no_of_rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print(len(no_of_rows))
no_of_cols=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
print(len(no_of_cols))

# #2) read specific row and data.
#capturing master in selenium
m=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(m)


#3) read all rows and data
print("printing all rows and columns-------------------")

for r in range(2, no_of_rows+1):
    for c in range(1, no_of_cols+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)







