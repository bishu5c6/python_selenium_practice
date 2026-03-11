from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
cookies=driver.get_cookies()
print(cookies)
print(len(cookies))

# for i in cookies:
#     # print(i)
#     print(i.get("name"),":",i.get("value"))

#Add a new cookie to the browser
new_cookie=driver.add_cookie({"name":"bish","value":"123456"})
print(cookies)
print(len(cookies))

driver.delete_cookie(new_cookie)
#delete all the cookies

driver.delete_all_cookies()